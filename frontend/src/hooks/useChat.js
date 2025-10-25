/**
 * useChat Hook - Manages chat state and logic
 */

import { useState, useCallback } from 'react'
import { sendChatMessage } from '../services/chatService'

export const useChat = () => {
  const [messages, setMessages] = useState([])
  const [isLoading, setIsLoading] = useState(false)

  /**
   * Send a message to the chat
   */
  const sendMessage = useCallback(async (userInput) => {
    if (!userInput.trim() || isLoading) return

    const userMessage = {
      role: 'user',
      content: userInput.trim()
    }

    // Add user message to UI
    const updatedMessages = [...messages, userMessage]
    setMessages(updatedMessages)
    setIsLoading(true)

    try {
      const response = await sendChatMessage(updatedMessages)

      if (response.success) {
        const assistantMessage = {
          role: 'assistant',
          content: response.content,
          suggested_prompts: response.suggestedPrompts
        }
        setMessages([...updatedMessages, assistantMessage])
      } else {
        const errorMessage = {
          role: 'assistant',
          content: response.content,
          suggested_prompts: []
        }
        setMessages([...updatedMessages, errorMessage])
      }
    } catch (error) {
      console.error('Error in sendMessage:', error)
      const errorMessage = {
        role: 'assistant',
        content: 'Xin lỗi, đã có lỗi xảy ra. Vui lòng thử lại.',
        suggested_prompts: []
      }
      setMessages([...updatedMessages, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }, [messages, isLoading])

  /**
   * Clear all messages
   */
  const clearMessages = useCallback(() => {
    setMessages([])
  }, [])

  return {
    messages,
    isLoading,
    sendMessage,
    clearMessages
  }
}

