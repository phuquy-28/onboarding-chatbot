# Technical Context

## Technology Stack

### Backend
- **Language**: Python 3.9+
- **Framework**: Flask (lightweight REST API)
- **LLM SDK**: Azure OpenAI Python SDK
- **Dependencies**:
  - `openai` - Azure OpenAI client
  - `flask` - Web framework
  - `flask-cors` - Handle CORS for React frontend
  - `python-dotenv` - Environment variable management

### Frontend
- **Framework**: React 18+
- **Build Tool**: Vite
- **Styling**: Modern CSS with clean UI
- **HTTP Client**: Fetch API

## Project Structure
```
onboarding-chatbot/
├── backend/
│   ├── app.py              # Flask application
│   ├── mock_data.py        # Mock data definitions
│   ├── functions.py        # Function calling implementations
│   ├── requirements.txt    # Python dependencies
│   └── .env.example        # Environment variables template
├── frontend/
│   ├── src/
│   │   ├── App.jsx         # Main React component
│   │   ├── components/     # React components
│   │   └── main.jsx        # Entry point
│   ├── package.json
│   └── vite.config.js
└── memory-bank/            # Project documentation
```

## Development Setup
1. Backend runs on `http://localhost:5000`
2. Frontend runs on `http://localhost:5173` (Vite default)
3. CORS enabled for local development

## Azure OpenAI Configuration
Required environment variables:
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_DEPLOYMENT_NAME`
- `AZURE_OPENAI_API_VERSION`

