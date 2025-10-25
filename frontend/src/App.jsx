/**
 * Main App Component - Orchestrates the chat application
 */

import { useState, useCallback } from 'react'
import './App.css'

// Hooks
import { useChat } from './hooks/useChat'
import { useGreeting } from './hooks/useGreeting'

// Components
import ChatHeader from './components/ChatHeader'
import WelcomeScreen from './components/WelcomeScreen'
import MessageList from './components/MessageList'
import ChatInput from './components/ChatInput'

function App() {
  const { messages, isLoading, sendMessage, clearMessages } = useChat()
  const { greetingMessage } = useGreeting()
  const [inputValue, setInputValue] = useState('')

  // Handle sending message from input
  const handleSendMessage = useCallback((message) => {
    sendMessage(message)
  }, [sendMessage])

  // Handle suggestion click (from welcome screen or contextual chips)
  const handleSuggestionClick = useCallback((suggestion) => {
    setInputValue(suggestion)
  }, [])

  // Handle clear conversation
  const handleClearConversation = useCallback(() => {
    clearMessages()
  }, [clearMessages])

  return (
    <div className="app">
      <div className="chat-container">
        {/* Header */}
        <ChatHeader
          hasMessages={messages.length > 0}
          onClear={handleClearConversation}
        />

        {/* Messages Area */}
        <div className="messages-container">
          {messages.length === 0 ? (
            <WelcomeScreen
              greetingMessage={greetingMessage}
              onSuggestionClick={handleSuggestionClick}
            />
          ) : (
            <MessageList
              messages={messages}
              isLoading={isLoading}
              onSuggestionClick={handleSuggestionClick}
            />
          )}
        </div>

        {/* Input Area */}
        <ChatInput
          onSendMessage={handleSendMessage}
          isLoading={isLoading}
          inputValue={inputValue}
          setInputValue={setInputValue}
        />
      </div>
    </div>
  )
}

export default App
