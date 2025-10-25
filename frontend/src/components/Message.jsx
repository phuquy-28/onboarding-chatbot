/**
 * Message Component - Displays a single chat message
 */

import React, { useMemo } from 'react'
import { formatMessage } from '../utils/messageFormatter'
import SuggestionChips from './SuggestionChips'

const Message = React.memo(({ message, onSuggestionClick, isLoading }) => {
  const formattedContent = useMemo(
    () => formatMessage(message.content),
    [message.content]
  )

  const avatar = message.role === 'user' ? '👤' : '🤖'

  return (
    <div className={`message ${message.role}`}>
      <div className="message-avatar">{avatar}</div>
      <div className="message-content">
        <div
          className="message-text"
          dangerouslySetInnerHTML={{ __html: formattedContent }}
        />
        {message.role === 'assistant' && message.suggested_prompts?.length > 0 && (
          <SuggestionChips
            prompts={message.suggested_prompts}
            onChipClick={onSuggestionClick}
            disabled={isLoading}
          />
        )}
      </div>
    </div>
  )
})

Message.displayName = 'Message'

export default Message

