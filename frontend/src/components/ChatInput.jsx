/**
 * ChatInput Component - Input area for sending messages
 */

import React, { useCallback } from 'react'

const ChatInput = React.memo(({ onSendMessage, isLoading, inputValue, setInputValue }) => {
  const handleSend = useCallback(() => {
    if (inputValue.trim() && !isLoading) {
      onSendMessage(inputValue)
      setInputValue('')
    }
  }, [inputValue, isLoading, onSendMessage, setInputValue])

  const handleKeyPress = useCallback((e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }, [handleSend])

  return (
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
          onClick={handleSend}
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
  )
})

ChatInput.displayName = 'ChatInput'

export default ChatInput
