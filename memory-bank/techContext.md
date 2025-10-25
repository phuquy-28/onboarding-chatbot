# Technical Context

## Technology Stack

### Backend
- **Language**: Python 3.9+
- **Framework**: Flask (lightweight REST API)
- **LLM SDK**: Azure OpenAI Python SDK (openai==1.55.3)
- **Dependencies**:
  - `openai` - Azure OpenAI client
  - `flask` - Web framework
  - `flask-cors` - Handle CORS for React frontend
  - `python-dotenv` - Environment variable management

### Frontend
- **Framework**: React 18+
- **Build Tool**: Vite
- **Styling**: Modern CSS with gradients and animations
- **HTTP Client**: Fetch API
- **Rendering**: Markdown support with `dangerouslySetInnerHTML`
- **Performance**: React.memo, useMemo, useCallback optimizations

## Project Structure
```
onboarding-chatbot/
├── backend/
│   ├── app.py              # Flask application + format tool logic
│   ├── mock_data.py        # Mock data (9 organized sections)
│   ├── functions.py        # Function calling + FORMAT_RESPONSE_TOOL
│   ├── requirements.txt    # Python dependencies
│   └── .env.example        # Environment variables template
├── frontend/
│   ├── src/
│   │   ├── components/     # UI Components (7 files)
│   │   │   ├── ChatHeader.jsx
│   │   │   ├── WelcomeScreen.jsx
│   │   │   ├── MessageList.jsx
│   │   │   ├── Message.jsx
│   │   │   ├── SuggestionChips.jsx
│   │   │   ├── TypingIndicator.jsx
│   │   │   └── ChatInput.jsx
│   │   ├── hooks/          # Custom React Hooks (2 files)
│   │   │   ├── useChat.js
│   │   │   └── useGreeting.js
│   │   ├── services/       # API Layer (1 file)
│   │   │   └── chatService.js
│   │   ├── utils/          # Utility Functions (1 file)
│   │   │   └── messageFormatter.js
│   │   ├── App.jsx         # Main orchestrator (70 lines)
│   │   ├── App.css         # Styles
│   │   └── main.jsx        # Entry point
│   ├── package.json
│   └── vite.config.js
├── memory-bank/            # Project documentation
│   ├── activeContext.md
│   ├── progress.md
│   ├── systemPatterns.md
│   ├── techContext.md
│   ├── productContext.md
│   └── projectbrief.md
├── README.md               # Main documentation
├── IMPROVEMENTS.md         # Phase 1 changelog
├── USE_CASES.md           # Phase 2 use cases
├── CONTEXTUAL_SUGGESTIONS.md  # Phase 3 suggestions
├── HR_EXTENSION.md        # Phase 4 HR features
└── REFACTORING.md         # Phase 5 code refactoring ⭐ NEW
```

## Backend Architecture

### mock_data.py Structure (Refactored)
Organized into 9 clear sections:
1. **FAQ DATA** - Onboarding FAQs
2. **EMPLOYEE DATA** - Employee information
3. **ONBOARDING TASKS DATA** - Task lists
4. **TEAM DATA** - Team meetings and info
5. **IT/HR KNOWLEDGE BASE** - IT support, HR systems, office info
6. **HR POLICY DATA** - Compensation, benefits, leave, career
7. **LEAVE BALANCE DATA** - Employee leave balances
8. **TRAINING COURSES DATA** - Available courses
9. **HELPER FUNCTIONS** - Data access functions

**Benefits**:
- All data grouped together (sections 1-8)
- All functions grouped together (section 9)
- Easy to navigate and maintain

## Frontend Architecture (Refactored)

### Component Layer
**7 Focused Components** - Each with single responsibility:
- `ChatHeader.jsx` - App title and clear button
- `WelcomeScreen.jsx` - Greeting and 12 suggestion buttons
- `MessageList.jsx` - Message list with auto-scroll
- `Message.jsx` - Single message display
- `SuggestionChips.jsx` - Contextual suggestion buttons
- `TypingIndicator.jsx` - Loading animation
- `ChatInput.jsx` - Input area with send button

**Performance**: All components wrapped with `React.memo`

### Hook Layer
**2 Custom Hooks** - Reusable business logic:
- `useChat.js` - Manages chat state and message sending
- `useGreeting.js` - Fetches and manages greeting

### Service Layer
**1 Service** - API abstraction:
- `chatService.js` - All API calls (fetchGreeting, sendChatMessage)

### Utility Layer
**1 Utility** - Pure functions:
- `messageFormatter.js` - Markdown to HTML conversion

### Main App
**App.jsx** - Orchestrator (70 lines, reduced from 324)
- Uses custom hooks
- Passes props to components
- Handles user interactions

## Development Setup
1. Backend runs on `http://localhost:5000`
2. Frontend runs on `http://localhost:5173` (Vite default)
3. CORS enabled for local development

## Azure OpenAI Configuration
Required environment variables:
- `AZURE_OPENAI_ENDPOINT` - Your Azure OpenAI endpoint URL
- `AZURE_OPENAI_API_KEY` - API key for authentication
- `AZURE_OPENAI_DEPLOYMENT_NAME` - Deployment name (e.g., gpt-4)
- `AZURE_OPENAI_API_VERSION` - API version (2024-02-15-preview)

## API Endpoints

### POST /api/chat
Main chat endpoint with contextual suggestions.

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

## Key Implementation Details

### Format Tool Integration
- Defined in `backend/functions.py` as `FORMAT_RESPONSE_TOOL`
- Included in `ALL_TOOLS` array
- Forced via `function_call={"name": "format_user_response"}`
- Parsed in `backend/app.py` to extract structured output

### Contextual Suggestions
- Generated by LLM based on conversation context
- Always 3 suggestions per response
- Displayed as clickable chips in UI
- Click handler in `SuggestionChips.jsx` component

### Performance Optimizations
- **React.memo**: All components memoized
- **useMemo**: Expensive computations cached
- **useCallback**: Functions memoized for referential equality
- **Component Splitting**: Small, focused components
- **Latency**: +500-800ms per response (2 LLM calls)
- **Token Usage**: +80-150 tokens per interaction

## Dependencies

### Backend (requirements.txt)
```
Flask==3.0.0
flask-cors==4.0.0
openai==1.55.3
python-dotenv==1.0.0
```

### Frontend (package.json)
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.1",
    "vite": "^5.0.8"
  }
}
```
