"""
Flask backend for Employee Onboarding Chatbot
Handles Azure OpenAI integration and function calling
"""

import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import AzureOpenAI
from dotenv import load_dotenv

from mock_data import onboarding_faqs, mock_knowledge_base, mock_hr_policy
from functions import FUNCTION_DEFINITIONS, ALL_TOOLS, FORMAT_RESPONSE_TOOL, execute_function

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-07-01-preview",  # Use fixed version for stability
)

DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


def create_system_prompt():
    """
    Create enhanced system prompt with few-shot examples and formatting guidelines
    """
    base_prompt = """Bạn là Trợ lý Onboarding thông minh của FPT Software. Nhiệm vụ của bạn là hỗ trợ nhân viên mới trong quá trình onboarding một cách chủ động và hiệu quả.

## Tính cách
- Thân thiện, chuyên nghiệp, nhiệt tình
- Chủ động hỗ trợ, không chỉ đợi được hỏi
- Quan tâm đến deadline và sự tiến bộ của nhân viên

## Quy tắc trả lời

### 1. Định dạng phản hồi
- Sử dụng Markdown để định dạng rõ ràng
- Danh sách nhiệm vụ: dùng bullet points với emoji (✅ cho Done, ⏳ cho Pending)
- Thông tin liên lạc: hiển thị Email, Phone, Teams link rõ ràng
- Ngày tháng: format DD/MM/YYYY
- Priority: dùng emoji (🔴 High, 🟡 Medium, 🟢 Low)

### 2. Sử dụng Functions
- Khi người dùng hỏi về nhiệm vụ → gọi get_onboarding_tasks
- Khi người dùng hỏi về manager/buddy → gọi get_employee_info
- Khi người dùng báo hoàn thành task → gọi update_task_status
- Khi người dùng muốn kết nối với ai đó → gọi send_introduction_message

### 3. Chào hỏi chủ động
- Luôn gọi tên nhân viên khi biết thông tin
- Kiểm tra và nhắc về nhiệm vụ sắp đến hạn
- Đề xuất hành động tiếp theo

### 4. Xử lý không biết
- Nếu không rõ hoặc không có thông tin → đừng bịa đặt
- Đề xuất liên hệ với HR hoặc IT Support
- Format: "Em chưa có thông tin về [chủ đề]. Anh/chị có muốn em kết nối anh/chị với bộ phận [HR/IT] để được hỗ trợ không?"

## Ví dụ FAQ

"""
    
    # Add few-shot examples from FAQ
    for i, faq in enumerate(onboarding_faqs[:4], 1):
        base_prompt += f"**Q{i}:** {faq['q']}\n**A{i}:** {faq['a']}\n\n"
    
    base_prompt += """
## Ví dụ format phản hồi tốt

**Danh sách nhiệm vụ:**
✅ Gặp mặt Buddy (Hoàn thành)
⏳ Hoàn thành khóa học Security (Hạn: 25/10) - 🔴 Ưu tiên cao
⏳ Thiết lập môi trường dev (Hạn: 27/10) - 🟡 Ưu tiên trung bình

**Thông tin liên lạc:**
📧 Email: cuong.tran@fsoft.com.vn
📞 Phone: +84 93 456 7890
💬 [Chat trên Teams](https://teams.microsoft.com/l/chat/cuong.tran)

## Quy tắc Xác nhận (Confirmation)

**QUAN TRỌNG**: Trước khi gọi function `update_task_status`, PHẢI hỏi xác nhận:
1. Nhận diện task user muốn update
2. Hỏi xác nhận: "Em thấy có nhiệm vụ [tên task]. Anh xác nhận đã hoàn thành đúng không?"
3. CHỈ gọi function sau khi user xác nhận (ví dụ: "đúng", "yes", "ok")
4. Sau khi update, gọi `get_next_task` để gợi ý việc tiếp theo

**Ví dụ workflow:**
User: "Tôi hoàn thành khóa học Security rồi"
Bot: "Tuyệt vời! Em thấy nhiệm vụ **[T01] Hoàn thành khóa học Security Awareness**. Anh xác nhận đã hoàn thành nhiệm vụ này đúng không?"
User: "Đúng rồi"
Bot: [Gọi update_task_status] → [Gọi get_next_task] → Phản hồi với nhiệm vụ tiếp theo

## Knowledge Base - IT Support

"""
    
    # Add IT support knowledge
    for item in mock_knowledge_base["it_support"]:
        if "topic" in item:
            base_prompt += f"\n**{item['topic']}:**\n"
            for key, value in item.items():
                if key != "topic":
                    base_prompt += f"- {key.capitalize()}: {value}\n"
    
    base_prompt += "\n## Knowledge Base - HR Systems\n"
    
    # Add HR systems knowledge
    for item in mock_knowledge_base["hr_systems"]:
        base_prompt += f"\n**{item['name']}** ({item['system']}):\n"
        base_prompt += f"- Link: {item['link']}\n"
        base_prompt += f"- Mô tả: {item['description']}\n"
        if "approval" in item:
            base_prompt += f"- Phê duyệt: {item['approval']}\n"
        if "deadline" in item:
            base_prompt += f"- Deadline: {item['deadline']}\n"
        if "availability" in item:
            base_prompt += f"- Thời gian: {item['availability']}\n"
    
    base_prompt += "\n## Office Information\n"
    
    # Add office info
    for office in mock_knowledge_base["office_info"]:
        base_prompt += f"\n**{office['location']}:**\n"
        base_prompt += f"- Địa chỉ: {office['address']}\n"
        base_prompt += f"- Giờ làm việc: {office['working_hours']}\n"
        base_prompt += f"- Parking: {office['parking']}\n"
        base_prompt += f"- Canteen: {office['canteen']}\n"
    
    # ========== HR POLICY KNOWLEDGE BASE (Extended) ==========
    base_prompt += "\n\n## HR Policy - Lương & Phúc lợi (Compensation & Benefits)\n"
    for key, value in mock_hr_policy["compensation"].items():
        base_prompt += f"- **{key}**: {value}\n"
    
    base_prompt += "\n**Phúc lợi (Benefits):**\n"
    for key, value in mock_hr_policy["benefits"].items():
        base_prompt += f"- **{key}**: {value}\n"
    
    base_prompt += "\n## HR Policy - Nghỉ phép & Chấm công (Leave & Time-Off)\n"
    for key, value in mock_hr_policy["leave_policy"].items():
        base_prompt += f"- **{key}**: {value}\n"
    
    base_prompt += "\n## HR Policy - Đào tạo & Phát triển (Training & Career)\n"
    for key, value in mock_hr_policy["career"].items():
        base_prompt += f"- **{key}**: {value}\n"
    
    base_prompt += "\n## HR Policy - Hệ thống Nội bộ (Internal Systems)\n"
    for system, desc in mock_hr_policy["internal_systems"].items():
        base_prompt += f"- **{system}**: {desc}\n"
    
    base_prompt += "\n## HR Policy - Chính sách Chi phí (Expense Policy)\n"
    for key, value in mock_hr_policy["expense_policy"].items():
        base_prompt += f"- **{key}**: {value}\n"
    
    base_prompt += """

## Quy tắc Format Phản hồi (QUAN TRỌNG)

**BẮT BUỘC**: Sau khi hoàn thành tất cả các function calls cần thiết, PHẢI sử dụng tool `format_user_response` để:
1. Tạo câu trả lời chính (main_answer) với format đẹp
2. Đề xuất 3 câu hỏi/hành động tiếp theo CÓ LIÊN QUAN đến ngữ cảnh

**Ví dụ suggestions tốt:**
- Nếu vừa trả lời về tasks → Gợi ý: "Đánh dấu task hoàn thành", "Task nào sắp hết hạn?"
- Nếu vừa trả lời về team → Gợi ý: "Khi nào có meeting?", "Ai là team lead?"
- Nếu vừa trả lời về IT → Gợi ý: "Hướng dẫn cài VPN", "Liên hệ IT support"

Suggestions phải NGẮN GỌN (< 50 ký tự) và HÀNH ĐỘNG được.

Hãy áp dụng phong cách trên cho mọi phản hồi. Luôn nhớ XÁC NHẬN trước khi update task.
"""
    
    return base_prompt


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint
    Receives message history and returns assistant response
    """
    try:
        data = request.json
        messages = data.get('messages', [])
        
        if not messages:
            return jsonify({"error": "No messages provided"}), 400
        
        # Add system prompt if not present
        if not messages or messages[0].get("role") != "system":
            system_message = {
                "role": "system",
                "content": create_system_prompt()
            }
            messages.insert(0, system_message)
        
        # Step 1: Call Azure OpenAI with ALL tools (including format tool)
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=messages,
            functions=ALL_TOOLS,
            function_call="auto",
            temperature=0.7,
            max_tokens=800
        )
        
        response_message = response.choices[0].message
        
        # Check if LLM wants to call a function
        if response_message.function_call:
            function_name = response_message.function_call.name
            function_args = response_message.function_call.arguments
            
            # Case 1: Format tool - this is the final response
            if function_name == "format_user_response":
                try:
                    format_data = json.loads(function_args)
                    return jsonify({
                        "success": True,
                        "messages": messages,
                        "response": {
                            "role": "assistant",
                            "content": format_data.get("main_answer", ""),
                            "suggested_prompts": format_data.get("suggested_prompts", [])
                        }
                    })
                except json.JSONDecodeError:
                    # Fallback if format parsing fails
                    return jsonify({
                        "success": True,
                        "messages": messages,
                        "response": {
                            "role": "assistant",
                            "content": response_message.content or "Xin lỗi, có lỗi xảy ra.",
                            "suggested_prompts": []
                        }
                    })
            
            # Case 2: Real function call (get_employee_info, update_task, etc.)
            # Execute the function
            function_result = execute_function(function_name, function_args)
            
            # Add assistant's function call to messages
            messages.append({
                "role": "assistant",
                "content": None,
                "function_call": {
                    "name": function_name,
                    "arguments": function_args
                }
            })
            
            # Add function result to messages
            messages.append({
                "role": "function",
                "name": function_name,
                "content": json.dumps(function_result, ensure_ascii=False)
            })
            
            # Step 2: Call LLM again and FORCE it to use format tool
            second_response = client.chat.completions.create(
                model=DEPLOYMENT_NAME,
                messages=messages,
                functions=ALL_TOOLS,
                function_call={"name": "format_user_response"},  # Force format tool
                temperature=0.7,
                max_tokens=800
            )
            
            final_message = second_response.choices[0].message
            
            # Parse format tool response
            if final_message.function_call and final_message.function_call.name == "format_user_response":
                try:
                    format_data = json.loads(final_message.function_call.arguments)
                    return jsonify({
                        "success": True,
                        "messages": messages,
                        "response": {
                            "role": "assistant",
                            "content": format_data.get("main_answer", ""),
                            "suggested_prompts": format_data.get("suggested_prompts", [])
                        }
                    })
                except json.JSONDecodeError:
                    pass
            
            # Fallback
            return jsonify({
                "success": True,
                "messages": messages,
                "response": {
                    "role": "assistant",
                    "content": final_message.content or "Đã xử lý xong.",
                    "suggested_prompts": []
                }
            })
        
        # No function call - should not happen with format tool, but handle it
        return jsonify({
            "success": True,
            "messages": messages,
            "response": {
                "role": "assistant",
                "content": response_message.content or "Xin chào!",
                "suggested_prompts": []
            }
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/greeting', methods=['POST'])
def get_greeting():
    """
    Generate proactive greeting for a specific employee
    Checks for urgent tasks and creates personalized welcome message
    """
    try:
        data = request.json
        employee_id = data.get('employee_id', 'E123')  # Default to E123
        
        from functions import get_employee_info, check_urgent_tasks
        
        # Get employee info
        emp_result = get_employee_info(employee_id)
        if not emp_result.get("success"):
            return jsonify({
                "success": False,
                "error": "Employee not found"
            }), 404
        
        employee = emp_result["data"]
        name = employee["name"].split()[-1]  # Get first name
        
        # Check for urgent tasks
        urgent_result = check_urgent_tasks(employee_id)
        urgent_tasks = urgent_result.get("urgent_tasks", [])
        
        # Build greeting message
        greeting = f"👋 Chào {name}! Em là Trợ lý Onboarding của FPT Software.\n\n"
        
        if urgent_tasks:
            if len(urgent_tasks) == 1:
                task = urgent_tasks[0]
                days_text = "hôm nay" if task["days_left"] == 0 else f"trong {task['days_left']} ngày tới"
                greeting += f"⚠️ Em thấy có **{task['task']}** sắp đến hạn {days_text}. "
                greeting += "Anh nhớ hoàn thành nhé!\n\n"
            else:
                greeting += f"⚠️ Em thấy anh có **{len(urgent_tasks)} nhiệm vụ** sắp đến hạn. "
                greeting += "Anh có muốn xem chi tiết không?\n\n"
        
        greeting += "Em có thể giúp gì cho anh hôm nay?"
        
        return jsonify({
            "success": True,
            "greeting": greeting,
            "employee": {
                "id": employee_id,
                "name": employee["name"]
            },
            "urgent_tasks_count": len(urgent_tasks)
        })
        
    except Exception as e:
        print(f"Error generating greeting: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Employee Onboarding Chatbot API"
    })


if __name__ == '__main__':
    # Check for required environment variables
    required_vars = [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_DEPLOYMENT_NAME"
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("⚠️  Warning: Missing environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease create a .env file based on .env.example")
    else:
        print("✅ All environment variables loaded")
    
    # Get port from environment variable (for deployment) or default to 5000
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '0.0.0.0')
    
    print(f"\n🚀 Starting Flask server on {host}:{port}")
    app.run(debug=False, host=host, port=port)
