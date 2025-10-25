/**
 * ChatHeader Component - Displays chat header with title and clear button
 */

import React from 'react'

const ChatHeader = React.memo(({ hasMessages, onClear }) => {
  return (
    <div className="chat-header">
      <div className="header-content">
        <div className="header-title">
          <h1>🎯 FPT Software Onboarding Assistant</h1>
          <p>Trợ lý hỗ trợ nhân viên mới</p>
        </div>
        {hasMessages && (
          <button onClick={onClear} className="clear-btn">
            🗑️ Xóa hội thoại
          </button>
        )}
      </div>
    </div>
  )
})

ChatHeader.displayName = 'ChatHeader'

export default ChatHeader

