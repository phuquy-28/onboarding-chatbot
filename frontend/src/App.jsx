import { useState, useRef, useEffect } from 'react'
import './App.css'

const API_URL = 'http://localhost:5000/api'
const DEFAULT_EMPLOYEE_ID = 'E123'  // Default employee for demo

function App() {
  const [messages, setMessages] = useState([])
  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [isFirstLoad, setIsFirstLoad] = useState(true)
  const [greetingMessage, setGreetingMessage] = useState('')
  const messagesEndRef = useRef(null)

  // Auto-scroll to bottom when new messages arrive
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  // Fetch proactive greeting on first load
  useEffect(() => {
    if (isFirstLoad) {
      fetchGreeting()
      setIsFirstLoad(false)
    }
  }, [isFirstLoad])

  // Fetch proactive greeting from backend
  const fetchGreeting = async () => {
    try {
      const response = await fetch(`${API_URL}/greeting`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          employee_id: DEFAULT_EMPLOYEE_ID
        })
      })

      const data = await response.json()
      if (data.success) {
        setGreetingMessage(data.greeting)
      }
    } catch (error) {
      console.error('Error fetching greeting:', error)
      // Fallback greeting
      setGreetingMessage('👋 Xin chào! Em là Trợ lý Onboarding của FPT Software. Em có thể giúp gì cho bạn?')
    }
  }

  // Format message content with basic Markdown support
  const formatMessage = (content) => {
    if (!content) return ''
    
    // Convert **bold** to <strong>
    let formatted = content.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    
    // Convert line breaks
    formatted = formatted.replace(/\n/g, '<br/>')
    
    // Convert emoji lists
    formatted = formatted.replace(/^([✅⏳🔴🟡🟢📧📞💬⚠️])/gm, '$1')
    
    return formatted
  }

  // Send message to backend
  const sendMessage = async () => {
    if (!inputValue.trim() || isLoading) return

    const userMessage = {
      role: 'user',
      content: inputValue.trim()
    }

    // Add user message to UI
    const updatedMessages = [...messages, userMessage]
    setMessages(updatedMessages)
    setInputValue('')
    setIsLoading(true)

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          messages: updatedMessages
        })
      })

      const data = await response.json()

      if (data.success) {
        // Add assistant response to messages
        setMessages([...updatedMessages, data.response])
      } else {
        // Show error message
        setMessages([...updatedMessages, {
          role: 'assistant',
          content: `Xin lỗi, đã có lỗi xảy ra: ${data.error}`
        }])
      }
    } catch (error) {
      console.error('Error sending message:', error)
      setMessages([...updatedMessages, {
        role: 'assistant',
        content: 'Xin lỗi, không thể kết nối với server. Vui lòng kiểm tra lại backend.'
      }])
    } finally {
      setIsLoading(false)
    }
  }

  // Handle Enter key press
  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  // Clear conversation
  const clearConversation = () => {
    setMessages([])
  }

  return (
    <div className="app">
      <div className="chat-container">
        {/* Header */}
        <div className="chat-header">
          <div className="header-content">
            <div className="header-title">
              <h1>🎯 FPT Software Onboarding Assistant</h1>
              <p>Trợ lý hỗ trợ nhân viên mới</p>
            </div>
            {messages.length > 0 && (
              <button onClick={clearConversation} className="clear-btn">
                🗑️ Xóa hội thoại
              </button>
            )}
          </div>
        </div>

        {/* Messages Area */}
        <div className="messages-container">
          {messages.length === 0 ? (
            <div className="welcome-screen">
              <div className="welcome-content">
                <div 
                  className="greeting-message"
                  dangerouslySetInnerHTML={{ __html: formatMessage(greetingMessage) }}
                />
                <p className="help-text">Em có thể hỗ trợ bạn:</p>
                <div className="suggestions">
                  <button 
                    className="suggestion-btn"
                    onClick={() => setInputValue('Nhiệm vụ của tôi là gì?')}
                  >
                    📋 Nhiệm vụ của tôi là gì?
                  </button>
                  <button 
                    className="suggestion-btn"
                    onClick={() => setInputValue('Ai là buddy của tôi?')}
                  >
                    👥 Ai là buddy của tôi?
                  </button>
                  <button 
                    className="suggestion-btn"
                    onClick={() => setInputValue('Khi nào tôi nhận lương?')}
                  >
                    💰 Khi nào tôi nhận lương?
                  </button>
                  <button 
                    className="suggestion-btn"
                    onClick={() => setInputValue('Kết nối với buddy')}
                  >
                    💬 Kết nối với buddy
                  </button>
                  <button 
                    className="suggestion-btn"
                    onClick={() => setInputValue('Tôi đã hoàn thành khóa học Security')}
                  >
                    ✅ Đánh dấu task hoàn thành
                  </button>
                  <button 
                    className="suggestion-btn"
                    onClick={() => setInputValue('Có nhiệm vụ nào sắp hết hạn không?')}
                  >
                    ⏰ Kiểm tra deadline
                  </button>
                </div>
              </div>
            </div>
          ) : (
            <div className="messages-list">
              {messages.map((message, index) => (
                <div 
                  key={index} 
                  className={`message ${message.role}`}
                >
                  <div className="message-avatar">
                    {message.role === 'user' ? '👤' : '🤖'}
                  </div>
                  <div className="message-content">
                    <div 
                      className="message-text"
                      dangerouslySetInnerHTML={{ __html: formatMessage(message.content) }}
                    />
                  </div>
                </div>
              ))}
              {isLoading && (
                <div className="message assistant">
                  <div className="message-avatar">🤖</div>
                  <div className="message-content">
                    <div className="typing-indicator">
                      <span></span>
                      <span></span>
                      <span></span>
                    </div>
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>
          )}
        </div>

        {/* Input Area */}
        <div className="input-container">
          <div className="input-wrapper">
            <textarea
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Nhập câu hỏi của bạn..."
              rows="1"
              disabled={isLoading}
            />
            <button 
              onClick={sendMessage}
              disabled={!inputValue.trim() || isLoading}
              className="send-btn"
            >
              {isLoading ? '⏳' : '📤'}
            </button>
          </div>
          <div className="input-hint">
            Nhấn Enter để gửi, Shift + Enter để xuống dòng
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
