/**
 * MessageList Component - Displays list of messages with loading indicator
 */

import React, { useRef, useEffect } from 'react'
import Message from './Message'
import TypingIndicator from './TypingIndicator'

const MessageList = React.memo(({ messages, isLoading, onSuggestionClick }) => {
  const messagesEndRef = useRef(null)

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isLoading])

  return (
    <div className="messages-list">
      {messages.map((message, index) => (
        <Message
          key={index}
          message={message}
          onSuggestionClick={onSuggestionClick}
          isLoading={isLoading}
        />
      ))}
      {isLoading && <TypingIndicator />}
      <div ref={messagesEndRef} />
    </div>
  )
})

MessageList.displayName = 'MessageList'

export default MessageList

