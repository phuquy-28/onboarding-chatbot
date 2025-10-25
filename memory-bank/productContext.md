# Product Context

## Problem Statement
New employees at FPT Software face information overload during onboarding. They have common questions about policies, procedures, and their specific onboarding schedule. Currently, they need to:
- Search through multiple documents
- Wait for HR/manager responses
- Navigate various systems to find information

## Solution
An AI-powered chatbot that provides instant, accurate answers to onboarding questions and retrieves personalized task information.

## User Experience Goals

### Primary User: New Hire Employee
**Use Cases:**
1. **Quick FAQ Access**: "Khi nào tôi nhận lương?" → Instant answer
2. **Task Management**: "Nhiệm vụ của tôi là gì?" → Personalized task list
3. **Follow-up Questions**: Multi-turn conversations with context retention

### Desired Experience
- **Conversational**: Natural language interaction in Vietnamese
- **Instant**: No waiting for human responses
- **Accurate**: Reliable information from mock company data
- **Contextual**: Remembers previous messages in conversation

## Key Features

### 1. FAQ Bot
**Value**: Answers common questions instantly
**Questions covered**:
- Salary and payment schedules
- IT setup (email, tools)
- Leave policies
- Company procedures

### 2. Dynamic Task Queries
**Value**: Personalized onboarding guidance
**Capabilities**:
- Show all tasks for employee
- Filter by status (Pending/Done)
- Show due dates
- Identify manager and buddy

### 3. Multi-turn Conversation
**Value**: Natural dialogue flow
**Example**:
- User: "Nhiệm vụ của tôi là gì?"
- Bot: [Shows task list]
- User: "Nhiệm vụ đầu tiên khi nào hết hạn?"
- Bot: [Remembers context and answers about first task]

## Success Criteria
- Bot correctly answers FAQ questions
- Function calling successfully retrieves employee data
- Conversation maintains context across multiple turns
- UI is intuitive and responsive

