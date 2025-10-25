/**
 * Chat Service - Handles all API communications with backend
 */

// Use environment variable for API URL, fallback to localhost for development
const API_URL = (import.meta.env.VITE_API_URL || 'http://localhost:5000') + '/api'
const DEFAULT_EMPLOYEE_ID = 'E123'

/**
 * Fetch proactive greeting for employee
 * @param {string} employeeId - Employee ID
 * @returns {Promise<Object>} Greeting data
 */
export const fetchGreeting = async (employeeId = DEFAULT_EMPLOYEE_ID) => {
  try {
    const response = await fetch(`${API_URL}/greeting`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ employee_id: employeeId })
    })

    const data = await response.json()
    
    if (data.success) {
      return {
        success: true,
        greeting: data.greeting,
        urgentTasksCount: data.urgent_tasks_count
      }
    }
    
    throw new Error('Failed to fetch greeting')
  } catch (error) {
    console.error('Error fetching greeting:', error)
    return {
      success: false,
      greeting: '👋 Xin chào! Em là Trợ lý Onboarding của FPT Software. Em có thể giúp gì cho bạn?',
      urgentTasksCount: 0
    }
  }
}

/**
 * Send chat message to backend
 * @param {Array} messages - Message history
 * @returns {Promise<Object>} Response data
 */
export const sendChatMessage = async (messages) => {
  try {
    const response = await fetch(`${API_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ messages })
    })

    const data = await response.json()

    if (data.success) {
      return {
        success: true,
        content: data.response.content,
        suggestedPrompts: data.response.suggested_prompts || []
      }
    }
    
    throw new Error(data.error || 'Failed to send message')
  } catch (error) {
    console.error('Error sending message:', error)
    return {
      success: false,
      content: 'Xin lỗi, không thể kết nối với server. Vui lòng kiểm tra lại backend.',
      suggestedPrompts: [],
      error: error.message
    }
  }
}

export { DEFAULT_EMPLOYEE_ID }

