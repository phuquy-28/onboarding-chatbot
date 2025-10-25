/**
 * useGreeting Hook - Manages greeting state and fetching
 */

import { useState, useEffect } from 'react'
import { fetchGreeting } from '../services/chatService'

export const useGreeting = () => {
  const [greetingMessage, setGreetingMessage] = useState('')
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    const loadGreeting = async () => {
      setIsLoading(true)
      const result = await fetchGreeting()
      setGreetingMessage(result.greeting)
      setIsLoading(false)
    }

    loadGreeting()
  }, [])

  return { greetingMessage, isLoading }
}

