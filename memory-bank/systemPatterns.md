# System Patterns

## Architecture Overview

### Client-Server Pattern
```
React Frontend <--REST API--> Flask Backend <--SDK--> Azure OpenAI
```

### Message Flow
1. User types message in React UI
2. Frontend sends POST request to `/api/chat` with message history
3. Backend processes request:
   - Adds user message to conversation
   - Calls Azure OpenAI with ALL_TOOLS (including format tool)
   - Handles function calls if requested by LLM
   - Forces format_user_response for structured output
   - Returns assistant response with suggestions
4. Frontend updates UI with response and contextual chips

## Conversation Management

### Stateless API Design
- Frontend maintains full conversation history (`messages` array)
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
    # ... 7 more real functions
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

## Prompt Engineering

### System Prompt Strategy
- Define chatbot personality (friendly FPT Software assistant)
- Embed few-shot examples from FAQ mock data
- Include knowledge base (IT/HR support)
- Set guidelines for professional responses
- Instruct on format tool usage and suggestion generation

### Few-Shot Learning
Include sample Q&A pairs in system prompt to guide responses for common questions.

### Contextual Suggestion Guidelines
System prompt includes examples of good suggestions:
- Task-related: "Đánh dấu task hoàn thành", "Task nào sắp hết hạn?"
- Team-related: "Khi nào có meeting?", "Ai là team lead?"
- IT-related: "Hướng dẫn cài VPN", "Liên hệ IT support"

## State Management

### Frontend State
- `messages`: Full conversation history
- `inputValue`: Current user input
- `isLoading`: Loading indicator state
- `greetingMessage`: Proactive greeting text
- `isFirstLoad`: Controls greeting fetch

### Backend State
- Stateless (no session storage)
- Mock data in memory (resets on restart)
- Task updates persist during runtime only

## Error Handling

### Backend
- Try-catch around LLM calls
- Fallback responses if format parsing fails
- Graceful degradation (empty suggestions array)

### Frontend
- Error messages in chat UI
- Disabled state during loading
- Connection error handling
