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
- **Contextual Suggestions**: Smart suggestion buttons based on user needs

### 2. FAQ Bot
- Answers common onboarding questions instantly
- Uses system prompts and few-shot learning
- Covers topics: salary, IT setup, leave policies, procedures
- Graceful fallback for unknown questions with escalation path

### 3. Interactive Task Management
- **View Tasks**: Retrieves employee-specific onboarding tasks
- **Update Status**: Mark tasks as complete through conversation
- **Filter Tasks**: View by status (Pending/Done) or priority
- **Deadline Tracking**: See days remaining for each task

### 4. Connection & Communication
- **Buddy Introduction**: Get contact details (email, phone, Teams link)
- **Manager Info**: Access manager contact information
- **Send Introductions**: Mock feature to send introduction messages
- **Rich Contact Cards**: Well-formatted contact information

### 5. Multi-turn Conversations
- Maintains context across conversation turns
- Natural dialogue flow in Vietnamese
- Remembers previous messages and task references

## 🏗️ Architecture

```
┌─────────────┐      REST API      ┌─────────────┐      SDK      ┌──────────────┐
│   React     │ ◄───────────────► │   Flask     │ ◄───────────► │ Azure OpenAI │
│  Frontend   │   (JSON/HTTP)      │   Backend   │               │              │
└─────────────┘                    └─────────────┘               └──────────────┘
                                          │
                                          ▼
                                   ┌─────────────┐
                                   │  Mock Data  │
                                   │  (Python)   │
                                   └─────────────┘
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
│   ├── functions.py        # Function calling implementations
│   ├── mock_data.py        # Mock data (FAQs, employees, tasks)
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example        # Environment variables template
│   └── README.md
├── frontend/
│   ├── src/
│   │   ├── App.jsx         # Main React component
│   │   ├── App.css         # Chat UI styling
│   │   └── main.jsx        # Entry point
│   ├── package.json
│   └── README.md
├── memory-bank/            # Project documentation
│   ├── projectbrief.md
│   ├── productContext.md
│   ├── systemPatterns.md
│   ├── techContext.md
│   ├── activeContext.md
│   └── progress.md
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

The frontend connects to `http://localhost:5000/api` by default. To change this, edit the `API_URL` in `frontend/src/App.jsx`.

## 💡 Usage Examples

### Proactive Features

**Smart Greeting (Auto on Load):**
```
Bot: 👋 Chào An! Em là Trợ lý Onboarding của FPT Software.

⚠️ Em thấy có Hoàn thành khóa học Security Awareness sắp đến hạn trong 1 ngày tới. Anh nhớ hoàn thành nhé!

Em có thể giúp gì cho anh hôm nay?
```

### Sample Questions

**FAQ Questions:**
- "Khi nào tôi nhận lương?"
- "Làm sao để cài đặt email công ty?"
- "Chính sách nghỉ phép như thế nào?"
- "Giờ làm việc của công ty là gì?"

**Task Management:**
- "Nhiệm vụ của tôi là gì?"
- "Nhiệm vụ nào còn pending?"
- "Tôi đã hoàn thành khóa học Security" _(Updates task status)_
- "Có nhiệm vụ nào sắp hết hạn không?"

**Connection & Communication:**
- "Ai là buddy của tôi?" _(Shows full contact info)_
- "Kết nối với buddy" _(Sends introduction message)_
- "Ai là quản lý của tôi?"
- "Làm sao liên lạc với manager?"

**Multi-turn Conversation:**
1. User: "Nhiệm vụ của tôi là gì?"
2. Bot: [Shows formatted task list with emojis]
3. User: "Tôi đã hoàn thành nhiệm vụ đầu tiên"
4. Bot: [Updates task status and confirms]
5. User: "Còn mấy nhiệm vụ chưa làm?"
6. Bot: [Shows remaining pending tasks]

## 📊 Mock Data

The system includes mock data for demonstration:

- **6 FAQ entries**: Common onboarding questions
- **3 employees**: E123 (Nguyễn Văn An), E456 (Đặng Phú Quý), E789 (Hoàng Thị Giang)
- **Onboarding tasks**: 3-5 tasks per employee with due dates and status

Default test employee: **E123 (Nguyễn Văn An)**

## 🎨 UI Features

- **Modern Design**: Gradient background with clean white chat interface
- **Smooth Animations**: Fade-in effects and typing indicators
- **Responsive Layout**: Works on desktop and mobile
- **Suggestion Buttons**: Quick access to common questions
- **Auto-scroll**: Automatically scrolls to latest message
- **Clear Conversation**: Reset chat with one click

## 🔍 API Endpoints

### POST /api/chat
Main chat endpoint for conversation.

**Request:**
```json
{
  "messages": [
    {"role": "user", "content": "Khi nào tôi nhận lương?"}
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
    "content": "Lương thử việc được trả vào ngày 15..."
  }
}
```

### GET /api/health
Health check endpoint.

## 🛠️ Technologies Used

### Backend
- **Python 3.9+**
- **Flask** - Web framework
- **Azure OpenAI SDK** - LLM integration
- **Flask-CORS** - Cross-origin support
- **python-dotenv** - Environment management

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool
- **Modern CSS** - Styling with gradients and animations

## 📝 Workshop Objectives

This project demonstrates:
1. ✅ **Prompt Engineering** - System prompts with few-shot examples
2. ✅ **Function Calling** - Dynamic data retrieval from mock database
3. ✅ **Multi-turn Conversations** - Context management across turns
4. ✅ **Message Management** - Proper handling of conversation history
5. ✅ **Modern UI** - Beautiful and responsive chat interface

## 🤝 Contributing

This is a workshop project. Feel free to:
- Add more FAQ entries in `backend/mock_data.py`
- Add more employees and tasks
- Enhance the UI with additional features
- Improve prompt engineering

## 📄 License

This project is for educational purposes as part of an Azure OpenAI workshop.

## 🙋 Support

For questions or issues:
1. Check the Memory Bank documentation in `memory-bank/`
2. Review the README files in `backend/` and `frontend/`
3. Ensure Azure OpenAI credentials are correctly configured

---

**Built with ❤️ for FPT Software Onboarding Workshop**

