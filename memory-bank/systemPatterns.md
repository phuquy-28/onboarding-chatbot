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
   - Calls Azure OpenAI with function definitions
   - Handles function calls if requested by LLM
   - Returns assistant response
4. Frontend updates UI with response

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

## Function Calling Pattern

### Function Registration
```python
functions = [
    {
        "name": "get_employee_info",
        "description": "Get information about an employee",
        "parameters": {...}
    },
    {
        "name": "get_onboarding_tasks",
        "description": "Get onboarding tasks for an employee",
        "parameters": {...}
    }
]
```

### Execution Flow
1. LLM decides to call function
2. Backend extracts function name and arguments
3. Backend executes Python function with mock data
4. Result added to messages as `role: function`
5. Second LLM call to generate natural language response

## Prompt Engineering

### System Prompt Strategy
- Define chatbot personality (friendly FPT Software assistant)
- Embed few-shot examples from FAQ mock data
- Set guidelines for professional responses

### Few-Shot Learning
Include sample Q&A pairs in system prompt to guide responses for common questions.

