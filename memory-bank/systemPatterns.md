# System Patterns

## Architecture Overview

### Client-Server Pattern
```
React Frontend <--REST API--> Flask Backend <--SDK--> Azure OpenAI
```

### Message Flow
1. User types message in `ChatInput` component
2. `ChatInput` calls `onSendMessage` prop
3. `App.jsx` calls `sendMessage` from `useChat` hook
4. `useChat` calls `sendChatMessage` from `chatService`
5. `chatService` sends POST to `/api/chat`
6. Backend processes request:
   - Adds user message to conversation
   - Calls Azure OpenAI with ALL_TOOLS (including format tool)
   - Handles function calls if requested by LLM
   - Forces format_user_response for structured output
   - Returns assistant response with suggestions
7. `chatService` returns response to `useChat`
8. `useChat` updates messages state
9. React re-renders `MessageList` with new message
10. `Message` component displays content and `SuggestionChips`

## Conversation Management

### Stateless API Design
- Frontend maintains full conversation history (`messages` array in `useChat`)
- Each API request includes complete message history
- Backend processes and returns updated messages

### Message Structure (OpenAI Format)
```python
{
    "role": "system|user|assistant|function",
    "content": "message content",
    "name": "function_name",  # for function role
    "function_call": {        # for assistant role
        "name": "function_name",
        "arguments": "{...}"
    }
}
```

### Frontend Message Structure
```javascript
{
  role: 'user' | 'assistant',
  content: 'message text',
  suggested_prompts: ['prompt1', 'prompt2', 'prompt3']  // Only for assistant
}
```

### Response Structure (with Suggestions)
```json
{
  "success": true,
  "messages": [...],
  "response": {
    "role": "assistant",
    "content": "Main answer with Markdown...",
    "suggested_prompts": [
      "Contextual suggestion 1",
      "Contextual suggestion 2",
      "Contextual suggestion 3"
    ]
  }
}
```

## Function Calling Pattern

### Function Registration
```python
ALL_TOOLS = [
    FORMAT_RESPONSE_TOOL,  # Virtual tool for structured output
    {
        "name": "get_employee_info",
        "description": "Get information about an employee",
        "parameters": {...}
    },
    {
        "name": "get_onboarding_tasks",
        "description": "Get onboarding tasks for an employee",
        "parameters": {...}
    },
    # ... 9 more real functions
]
```

### Execution Flow (2 Patterns)

#### Pattern 1: Direct Response (FAQ)
```
User asks FAQ
→ LLM calls format_user_response directly
→ Backend parses JSON
→ Returns {main_answer, suggested_prompts}
```

#### Pattern 2: Function Call First (Dynamic Data)
```
User asks about tasks
→ LLM calls get_onboarding_tasks
→ Backend executes function, gets data
→ Backend adds result to messages
→ Backend FORCES format_user_response
→ LLM generates natural answer + contextual suggestions
→ Backend parses JSON
→ Returns {main_answer, suggested_prompts}
```

### Format Tool Pattern
- **Purpose**: Force LLM to return structured JSON output
- **Type**: Virtual function (no Python execution)
- **Output Schema**:
  ```python
  {
    "main_answer": "string (Markdown formatted)",
    "suggested_prompts": ["string", "string", "string"]
  }
  ```
- **Benefit**: Every response includes 3 contextual suggestions

## Component Patterns (Frontend)

### Presentational Components
Pure UI components with no business logic:
- `ChatHeader` - Display only
- `TypingIndicator` - Display only
- `SuggestionChips` - Display + click handler

### Container Components
Components with logic:
- `App.jsx` - Main orchestrator
- `MessageList` - Auto-scroll logic
- `ChatInput` - Input handling logic

### Custom Hooks Pattern
Reusable stateful logic:
```javascript
// useChat.js
export const useChat = () => {
  const [messages, setMessages] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  
  const sendMessage = useCallback(async (input) => {
    // Business logic here
  }, [messages, isLoading])
  
  return { messages, isLoading, sendMessage, clearMessages }
}
```

### Service Layer Pattern
API abstraction:
```javascript
// chatService.js
export const sendChatMessage = async (messages) => {
  try {
    const response = await fetch(`${API_URL}/chat`, {...})
    const data = await response.json()
    return { success: true, content: data.response.content, ... }
  } catch (error) {
    return { success: false, content: 'Error message', ... }
  }
}
```

## Prompt Engineering

### System Prompt Strategy
- Define chatbot personality (friendly FPT Software assistant)
- Embed few-shot examples from FAQ mock data
- Include knowledge base (IT/HR support, policies)
- Set guidelines for professional responses
- Instruct on format tool usage and suggestion generation

### Few-Shot Learning
Include sample Q&A pairs in system prompt to guide responses for common questions.

### Contextual Suggestion Guidelines
System prompt includes examples of good suggestions:
- Task-related: "Đánh dấu task hoàn thành", "Task nào sắp hết hạn?"
- Team-related: "Khi nào có meeting?", "Ai là team lead?"
- IT-related: "Hướng dẫn cài VPN", "Liên hệ IT support"
- HR-related: "Số dư phép của tôi?", "Tìm khóa học về React"

## State Management

### Frontend State (React)

**App Level** (App.jsx):
- `inputValue` - Current input text
- Callbacks for child components

**useChat Hook**:
- `messages` - Full conversation history
- `isLoading` - Loading indicator state
- `sendMessage()` - Send message function
- `clearMessages()` - Clear conversation function

**useGreeting Hook**:
- `greetingMessage` - Proactive greeting text
- `isLoading` - Greeting fetch state

**Component Local State**:
- `ChatInput` - None (controlled by App)
- `WelcomeScreen` - None (stateless)
- `MessageList` - Auto-scroll ref

### Backend State
- Stateless (no session storage)
- Mock data in memory (resets on restart)
- Task updates persist during runtime only

## Performance Patterns

### React.memo
All components wrapped to prevent unnecessary re-renders:
```javascript
const ChatHeader = React.memo(({ hasMessages, onClear }) => {
  // Only re-renders if props change
})
```

### useMemo
Expensive computations memoized:
```javascript
const formattedGreeting = useMemo(
  () => formatMessage(greetingMessage),
  [greetingMessage]
)
```

### useCallback
Functions memoized for referential equality:
```javascript
const handleSendMessage = useCallback((message) => {
  sendMessage(message)
}, [sendMessage])
```

### Component Splitting
- Small, focused components (average 50 lines)
- Single responsibility principle
- Easier for React to optimize

## Error Handling

### Backend
- Try-catch around LLM calls
- Fallback responses if format parsing fails
- Graceful degradation (empty suggestions array)

### Frontend Service Layer
```javascript
try {
  const response = await fetch(...)
  return { success: true, ... }
} catch (error) {
  console.error('Error:', error)
  return { success: false, content: 'Error message', ... }
}
```

### Frontend UI
- Error messages displayed in chat
- Disabled state during loading
- Connection error handling
- Fallback greeting if fetch fails

## Data Flow Patterns

### Unidirectional Data Flow
```
User Action → Event Handler → Hook → Service → API
                                ↓
                            State Update
                                ↓
                            Re-render
```

### Props Drilling (Minimal)
- Max 2 levels deep
- Most state managed by hooks
- Callbacks passed as props

### Separation of Concerns
- **Components**: UI rendering
- **Hooks**: Business logic & state
- **Services**: API communication
- **Utils**: Pure functions
