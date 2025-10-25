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

from mock_data import onboarding_faqs
from functions import FUNCTION_DEFINITIONS, execute_function

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

Hãy áp dụng phong cách trên cho mọi phản hồi.
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
        
        # Call Azure OpenAI with function definitions
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=messages,
            functions=FUNCTION_DEFINITIONS,
            function_call="auto",
            temperature=0.7,
            max_tokens=800
        )
        
        response_message = response.choices[0].message
        
        # Check if LLM wants to call a function
        if response_message.function_call:
            function_name = response_message.function_call.name
            function_args = response_message.function_call.arguments
            
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
            
            # Call LLM again to generate natural language response
            second_response = client.chat.completions.create(
                model=DEPLOYMENT_NAME,
                messages=messages,
                temperature=0.7,
                max_tokens=800
            )
            
            final_message = second_response.choices[0].message
            
            return jsonify({
                "success": True,
                "messages": messages,
                "response": {
                    "role": "assistant",
                    "content": final_message.content
                }
            })
        
        # No function call - return direct response
        return jsonify({
            "success": True,
            "messages": messages,
            "response": {
                "role": "assistant",
                "content": response_message.content
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
    
    print("\n🚀 Starting Flask server on http://localhost:5000")
    app.run(debug=True, port=5000)
