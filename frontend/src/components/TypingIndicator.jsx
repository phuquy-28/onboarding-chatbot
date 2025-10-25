/**
 * TypingIndicator Component - Shows typing animation while loading
 */

import React from 'react'

const TypingIndicator = React.memo(() => (
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
))

TypingIndicator.displayName = 'TypingIndicator'

export default TypingIndicator

