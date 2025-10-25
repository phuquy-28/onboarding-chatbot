# Backend - Employee Onboarding Chatbot

Flask backend with Azure OpenAI integration for the Employee Onboarding Chatbot.

## Setup

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

## API Endpoints

### POST /api/chat
Main chat endpoint that handles conversations with Azure OpenAI.

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

## Project Structure

```
backend/
├── app.py              # Flask application and routes
├── functions.py        # Function calling implementations
├── mock_data.py        # Mock data (FAQs, employees, tasks)
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md          # This file
```

## Features

- **FAQ Bot**: Answers common questions using system prompts and few-shot learning
- **Function Calling**: Retrieves employee info and onboarding tasks dynamically
- **Multi-turn Conversations**: Maintains context across conversation turns
- **CORS Enabled**: Works with React frontend on different port

## Mock Data

The system includes mock data for:
- 6 common FAQ questions
- 3 sample employees (E123, E456, E789)
- Onboarding tasks for each employee

Default employee for testing: **E123 (Nguyễn Văn An)**

