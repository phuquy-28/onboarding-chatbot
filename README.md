# 🎯 Employee Onboarding Chatbot

An AI-powered chatbot application to assist new employees at FPT Software during their onboarding process. Built with React, Flask, and Azure OpenAI.

![Tech Stack](https://img.shields.io/badge/React-18-blue)
![Tech Stack](https://img.shields.io/badge/Flask-3.0-green)
![Tech Stack](https://img.shields.io/badge/Azure_OpenAI-Latest-orange)
![Tech Stack](https://img.shields.io/badge/Python-3.9+-yellow)

## ✨ Features

### 1. Proactive & Personalized Experience
- **Smart Greeting**: Bot greets employees by name and checks for urgent tasks
- **Deadline Reminders**: Proactively alerts about tasks due soon
- **Rich Formatting**: Uses Markdown with emojis for clear, organized responses
- **Contextual Suggestion Chips**: AI-generated follow-up suggestions after each response

### 2. FAQ Bot
- Answers common onboarding questions instantly
- Uses system prompts and few-shot learning
- Covers topics: salary, IT setup, leave policies, procedures, HR systems
- Graceful fallback for unknown questions with escalation path

### 3. Interactive Task Management
- **View Tasks**: Retrieves employee-specific onboarding tasks
- **Update Status**: Mark tasks as complete through conversation with confirmation
- **Filter Tasks**: View by status (Pending/Done) or priority
- **Deadline Tracking**: See days remaining for each task
- **Next Task Suggestions**: Get recommended next task after completion

### 4. Team Integration
- **Team Information**: View team details, lead, and member count
- **Meeting Schedules**: See all team meetings with Teams links
- **Collaboration**: 3 teams with recurring meeting schedules

### 5. Connection & Communication
- **Buddy Introduction**: Get contact details (email, phone, Teams link)
- **Manager Info**: Access manager contact information
- **Send Introductions**: Mock feature to send introduction messages
- **Rich Contact Cards**: Well-formatted contact information

### 6. HR & IT Support
- **Leave Management**: Check leave balance, understand leave policies
- **Training & Career**: Search courses, career development information
- **IT Support**: WiFi, VPN, email setup, hardware issues
- **HR Systems**: F-Leave, F-Timesheet, F-Pay, F-Learning guides
- **Compensation & Benefits**: Salary policies, benefits information

### 7. Multi-turn Conversations
- Maintains context across conversation turns
- Natural dialogue flow in Vietnamese
- Remembers previous messages and task references
- AI-generated contextual suggestions guide the conversation

## 🏗️ Architecture

```
┌─────────────────┐   REST API   ┌─────────────────┐   SDK   ┌──────────────┐
│  React Frontend │ ◄──────────► │  Flask Backend  │ ◄─────► │ Azure OpenAI │
│  (Refactored)   │  (JSON/HTTP) │                 │         │              │
└─────────────────┘              └─────────────────┘         └──────────────┘
                                          │
                                          ▼
                                  ┌──────────────┐
                                  │  Mock Data   │
                                  │  (9 sections)│
                                  └──────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- Azure OpenAI account with API credentials

### 1. Setup Backend

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your Azure OpenAI credentials

# Run the Flask server
python app.py
```

Backend will start on `http://localhost:5000`

### 2. Setup Frontend

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```

Frontend will start on `http://localhost:5173`

### 3. Open the Application

Open your browser and go to `http://localhost:5173`

## 📁 Project Structure

```
onboarding-chatbot/
├── backend/
│   ├── app.py              # Flask application & routes
│   ├── functions.py        # 11 function calling implementations
│   ├── mock_data.py        # Mock data
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example        # Environment variables template
│   └── README.md           # Backend documentation
├── frontend/
│   ├── src/
│   │   ├── components/     # UI Components
│   │   │   ├── ChatHeader.jsx
│   │   │   ├── WelcomeScreen.jsx
│   │   │   ├── MessageList.jsx
│   │   │   ├── Message.jsx
│   │   │   ├── SuggestionChips.jsx
│   │   │   ├── TypingIndicator.jsx
│   │   │   └── ChatInput.jsx
│   │   ├── hooks/          # Custom React Hooks
│   │   │   ├── useChat.js
│   │   │   └── useGreeting.js
│   │   ├── services/       # API Layer
│   │   │   └── chatService.js
│   │   ├── utils/          # Utility Functions
│   │   │   └── messageFormatter.js
│   │   ├── App.jsx         # Main orchestrator
│   │   ├── App.css         # Styles
│   │   └── main.jsx        # Entry point
│   ├── package.json
│   ├── vite.config.js
│   └── README.md           # Frontend documentation
├── memory-bank/            # Project documentation
│   ├── projectbrief.md
│   ├── productContext.md
│   ├── systemPatterns.md
│   ├── techContext.md
│   ├── activeContext.md
│   └── progress.md
├── IMPROVEMENTS.md         # Phase 1: UX/Utility enhancements
├── USE_CASES.md           # Phase 2: Use case implementations
├── CONTEXTUAL_SUGGESTIONS.md  # Phase 3: Suggestion chips
├── HR_EXTENSION.md        # Phase 4: HR features
├── REFACTORING.md         # Phase 5: Code refactoring
└── README.md              # This file
```

## 🔧 Configuration

### Backend Environment Variables

Create a `.env` file in the `backend/` directory:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

### Frontend API Configuration

The frontend connects to `http://localhost:5000/api` by default. To change this, edit the `API_URL` in `frontend/src/services/chatService.js`.

## 💡 Usage Examples

### Proactive Features

**Smart Greeting (Auto on Load):**
```
Bot: 👋 Chào An! Em là Trợ lý Onboarding của FPT Software.

⚠️ Em thấy có 2 nhiệm vụ sắp đến hạn:
- Hoàn thành khóa học Security Awareness (còn 1 ngày)
- Hoàn thành Code of Conduct training (còn 2 ngày)

Em có thể giúp gì cho anh hôm nay?

[Suggestion Chips: "Xem nhiệm vụ" | "Đánh dấu hoàn thành" | "Ai là buddy?"]
```

### Sample Questions

**FAQ Questions:**
- "Khi nào tôi nhận lương?"
- "Làm sao để cài đặt email công ty?"
- "Chính sách nghỉ phép như thế nào?"
- "Giờ làm việc của công ty là gì?"
- "Quy trình đánh giá hiệu suất?"

**Task Management:**
- "Nhiệm vụ của tôi là gì?"
- "Nhiệm vụ nào còn pending?"
- "Tôi đã hoàn thành khóa học Security" _(Updates task status with confirmation)_
- "Có nhiệm vụ nào sắp hết hạn không?"
- "Nhiệm vụ tiếp theo của tôi là gì?"

**Team Integration:**
- "Team của tôi có lịch họp gì?"
- "Khi nào có meeting?"
- "Ai là team lead?"

**Connection & Communication:**
- "Ai là buddy của tôi?" _(Shows full contact info)_
- "Kết nối với buddy" _(Sends introduction message)_
- "Ai là quản lý của tôi?"
- "Làm sao liên lạc với manager?"

**HR & IT Support:**
- "Tôi còn bao nhiêu ngày phép?"
- "Có khóa học nào về React không?"
- "Không vào được wifi F-town 3"
- "Hướng dẫn cài VPN"
- "Khi nào tôi nhận lương?"

**Multi-turn Conversation:**
1. User: "Nhiệm vụ của tôi là gì?"
2. Bot: [Shows formatted task list with emojis and contextual suggestions]
3. User: "Tôi đã hoàn thành nhiệm vụ đầu tiên"
4. Bot: [Asks for confirmation]
5. User: "Có, xác nhận"
6. Bot: [Updates task status, suggests next task]

## 📊 Mock Data

The system includes comprehensive mock data organized into 9 sections:

1. **FAQ Data**: 6 common onboarding questions
2. **Employee Data**: 3 employees with full contact info
   - E123 (Nguyễn Văn An) - Cloud Warriors
   - E456 (Đặng Phú Quý) - Monorepo Avengers
   - E789 (Hoàng Thị Giang) - Agile Ninjas
3. **Onboarding Tasks**: 12+ tasks with priorities and due dates
4. **Team Data**: 3 teams with meeting schedules
5. **IT/HR Knowledge Base**: 11 entries (WiFi, VPN, HR systems, office info)
6. **HR Policy Data**: 32 policies (compensation, benefits, leave, career)
7. **Leave Balance Data**: Leave balances for all employees
8. **Training Courses**: 8 courses (5 technical, 3 soft skills)
9. **Helper Functions**: 8 data access functions

Default test employee: **E123 (Nguyễn Văn An)** from Cloud Warriors team

## 🎨 UI Features

- **Modern Design**: Gradient background with clean white chat interface
- **Smooth Animations**: Fade-in effects and typing indicators
- **Responsive Layout**: Works on desktop and mobile
- **Welcome Screen**: 12 static suggestion buttons for quick access
- **Contextual Chips**: 3 dynamic AI-generated suggestions per response
- **Auto-scroll**: Automatically scrolls to latest message
- **Clear Conversation**: Reset chat with one click
- **Performance Optimized**: React.memo, useMemo, useCallback

## 🔍 API Endpoints

### POST /api/chat
Main chat endpoint for conversation with contextual suggestions.

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

## 🛠️ Technologies Used

### Backend
- **Python 3.9+**
- **Flask 3.0** - Web framework
- **Azure OpenAI SDK (1.55.3)** - LLM integration
- **Flask-CORS** - Cross-origin support
- **python-dotenv** - Environment management

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool
- **Modern CSS** - Styling with gradients and animations
- **Markdown rendering** - Rich text formatting
- **Performance Optimizations** - React.memo, useMemo, useCallback

### Architecture
- **11 Functions**: 10 real functions + 1 format tool
- **Modular Components**: 7 focused UI components
- **Custom Hooks**: 2 hooks for business logic
- **Service Layer**: API abstraction
- **Mock Data**: In-memory storage with 9 organized sections

## 📝 Workshop Objectives

This project demonstrates:
1. ✅ **Prompt Engineering** - System prompts with few-shot examples + embedded knowledge
2. ✅ **Function Calling** - 11 functions for dynamic data retrieval
3. ✅ **Multi-turn Conversations** - Context management with confirmation workflows
4. ✅ **Message Management** - Proper handling of conversation history
5. ✅ **Modern UI** - Proactive, beautiful and responsive chat interface
6. ✅ **Real-world Use Cases** - Task management, team integration, HR support
7. ✅ **Code Quality** - Modular architecture, performance optimizations

## 📚 Additional Documentation

- **IMPROVEMENTS.md** - Phase 1: UX/Utility enhancements changelog
- **USE_CASES.md** - Phase 2: Comprehensive use case implementations
- **CONTEXTUAL_SUGGESTIONS.md** - Phase 3: Contextual suggestion chips
- **HR_EXTENSION.md** - Phase 4: HR features (leave, training, policies)
- **REFACTORING.md** - Phase 5: Code refactoring (modular architecture)
- **memory-bank/** - Complete project documentation and context

## 🤝 Contributing

This is a workshop project. Feel free to:
- Add more FAQ entries in `backend/mock_data.py`
- Add more employees, teams, and tasks
- Create new components in `frontend/src/components/`
- Enhance the UI with additional features
- Improve prompt engineering
- Add unit tests

## 📄 License

This project is for educational purposes as part of an Azure OpenAI workshop.

## 🙋 Support

For questions or issues:
1. Check the documentation files (IMPROVEMENTS.md, USE_CASES.md, etc.)
2. Review the Memory Bank documentation in `memory-bank/`
3. Check the README files in `backend/` and `frontend/`
4. Ensure Azure OpenAI credentials are correctly configured