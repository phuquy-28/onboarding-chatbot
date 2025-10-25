# Backend - Employee Onboarding Chatbot

Flask backend with Azure OpenAI integration for the Employee Onboarding Chatbot.

## 🚀 Quick Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Configure environment variables:**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your Azure OpenAI credentials
```

3. **Run the server:**
```bash
python app.py
```

The server will start on `http://localhost:5000`

## 📁 Project Structure

```
backend/
├── app.py              # Flask application, routes, and LLM orchestration
├── functions.py        # 11 function calling implementations
├── mock_data.py        # Mock data organized into 9 sections
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md          # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

## 🔍 API Endpoints

### POST /api/chat
Main chat endpoint that handles conversations with Azure OpenAI.

**Request:**
```json
{
  "messages": [
    {"role": "user", "content": "Nhiệm vụ của tôi là gì?"}
  ]
}
```

**Response:**
```json
{
  "success": true,
  "messages": [...],
  "response": {
    "role": "assistant",
    "content": "Đây là các nhiệm vụ của anh...",
    "suggested_prompts": [
      "Đánh dấu task hoàn thành",
      "Task nào sắp hết hạn?",
      "Ai là buddy của tôi?"
    ]
  }
}
```

### POST /api/greeting
Generate personalized greeting with deadline alerts.

**Request:**
```json
{
  "employee_id": "E123"
}
```

**Response:**
```json
{
  "success": true,
  "greeting": "👋 Chào An! Em là Trợ lý Onboarding...",
  "urgent_tasks_count": 2
}
```

### GET /api/health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "message": "Backend is running"
}
```

## 📊 Mock Data Structure

The `mock_data.py` file is organized into 9 clear sections:

### Section 1: FAQ Data
- 6 common onboarding questions and answers
- Used for few-shot learning in system prompt

### Section 2: Employee Data
- 3 employees: E123, E456, E789
- Each with: name, email, phone, manager, buddy, team, position
- Full contact information including Teams links

### Section 3: Onboarding Tasks Data
- 12+ tasks across all employees
- Each with: task_id, task, description, due_date, status, priority

### Section 4: Team Data
- 3 teams: Cloud Warriors, Monorepo Avengers, Agile Ninjas
- Team lead, member count, meeting schedules with Teams links

### Section 5: IT/HR Knowledge Base
- **IT Support**: WiFi, VPN, Email Setup, Hardware Issues
- **HR Systems**: F-Leave, F-Timesheet, F-Pay, F-Learning
- **Office Info**: F-town 2 & 3 details

### Section 6: HR Policy Data
- **Compensation**: Pay dates, payslip, OT policy, 13th month salary
- **Benefits**: Health insurance, wellness, health checks
- **Leave Policy**: Annual, sick, special, unpaid leave
- **Career**: Levels, review cycle, goal setting, promotion
- **Internal Systems**: F-Pay, F-Timesheet, F-Leave, etc.
- **Expense Policy**: Business trips, training, equipment

### Section 7: Leave Balance Data
- Leave balances for all employees
- Annual leave, sick leave, special leave tracking

### Section 8: Training Courses Data
- 8 courses: 5 technical, 3 soft skills
- Each with: id, name, type, category, platform, duration, level

### Section 9: Helper Functions
- `get_all_employee_ids()` - Get all employee IDs
- `get_employee_by_name()` - Find employee by name
- `get_urgent_tasks()` - Get tasks due soon
- `update_task_status_in_db()` - Update task status
- `find_task_by_name()` - Find task by partial name
- `get_leave_balance_from_db()` - Get leave balance
- `search_training_courses_in_db()` - Search courses

## ⚙️ Function Calling

The backend implements 11 functions:

### Core Functions (2)
1. `get_employee_info` - Get employee details
2. `get_onboarding_tasks` - Get task list

### UX Enhancement Functions (3)
3. `update_task_status` - Mark tasks complete (with confirmation)
4. `send_introduction_message` - Connect with buddy/manager
5. `check_urgent_tasks` - Deadline reminders

### Use Case Functions (2)
6. `get_team_meetings` - Team meeting schedules
7. `get_next_task` - Suggest next priority task

### Format Function (1)
8. `format_user_response` - Structured output with contextual suggestions

### HR Functions (2)
9. `get_leave_balance` - Leave balance information
10. `search_training_courses` - Course search

### Knowledge Base (1)
11. Embedded in system prompt - IT/HR/Policy support

## 🎯 Features

### 1. Prompt Engineering
- System prompt with chatbot personality
- Few-shot examples from FAQ data
- Embedded knowledge base (IT/HR support, policies)
- Guidelines for response formatting and suggestions

### 2. Function Calling
- Dynamic data retrieval from mock database
- Confirmation workflows for critical actions
- Multi-intent handling

### 3. Contextual Suggestions
- 2-step LLM calling pattern
- Format tool forces structured output
- AI-generated contextual follow-up prompts

### 4. Multi-turn Conversations
- Maintains full conversation history
- Context-aware responses
- Natural dialogue flow in Vietnamese

### 5. CORS Enabled
- Works with React frontend on different port
- Configured for local development

## 🛠️ Technologies

- **Python 3.9+**
- **Flask 3.0** - Web framework
- **Azure OpenAI SDK 1.55.3** - LLM integration
- **Flask-CORS 4.0** - Cross-origin support
- **python-dotenv 1.0** - Environment management

## 📝 Development Notes

### Default Employee
The system uses **E123 (Nguyễn Văn An)** as the default employee for testing.

### Mock Data Updates
Task status updates persist during runtime but reset when the server restarts.

### System Prompt
The system prompt is dynamically generated in `app.py` and includes:
- Chatbot personality and guidelines
- Few-shot examples from FAQ
- Embedded knowledge base
- HR policies (32 policies)
- Format tool instructions

### LLM Call Pattern
1. User message → Backend
2. Backend calls Azure OpenAI with ALL_TOOLS
3. If real function called → Execute → Add result → Force format_user_response
4. Parse structured output (main_answer + suggested_prompts)
5. Return to frontend

## 🧪 Testing

### Test with curl

**Health Check:**
```bash
curl http://localhost:5000/api/health
```

**Chat:**
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Nhiệm vụ của tôi là gì?"}]}'
```

**Greeting:**
```bash
curl -X POST http://localhost:5000/api/greeting \
  -H "Content-Type: application/json" \
  -d '{"employee_id": "E123"}'
```

## 📚 Additional Resources

- **Main README**: `../README.md` - Project overview
- **Frontend README**: `../frontend/README.md` - Frontend documentation
- **REFACTORING.md**: `../REFACTORING.md` - Code refactoring details
- **Memory Bank**: `../memory-bank/` - Complete project context

## 🔄 Recent Updates

### Code Organization
- ✅ `mock_data.py` refactored into 9 clear sections
- ✅ All data grouped together (sections 1-8)
- ✅ All functions grouped together (section 9)
- ✅ Better documentation with section headers

See `../REFACTORING.md` for detailed refactoring information.
