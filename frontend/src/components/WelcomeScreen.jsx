/**
 * WelcomeScreen Component - Initial welcome screen with greeting and suggestions
 */

import React, { useMemo } from 'react'
import { formatMessage } from '../utils/messageFormatter'

const SUGGESTION_BUTTONS = [
  { emoji: '📋', text: 'Nhiệm vụ của tôi là gì?', query: 'Nhiệm vụ của tôi là gì?' },
  { emoji: '👥', text: 'Ai là buddy của tôi?', query: 'Ai là buddy của tôi?' },
  { emoji: '💰', text: 'Khi nào tôi nhận lương?', query: 'Khi nào tôi nhận lương?' },
  { emoji: '💬', text: 'Kết nối với buddy', query: 'Kết nối với buddy' },
  { emoji: '✅', text: 'Đánh dấu task hoàn thành', query: 'Tôi đã hoàn thành khóa học Security' },
  { emoji: '⏰', text: 'Kiểm tra deadline', query: 'Có nhiệm vụ nào sắp hết hạn không?' },
  { emoji: '📅', text: 'Lịch họp team', query: 'Team của tôi có lịch họp gì?' },
  { emoji: '📶', text: 'Hỗ trợ IT', query: 'Không vào được wifi F-town 3' },
  { emoji: '🏖️', text: 'Số dư phép', query: 'Tôi còn bao nhiêu ngày phép?' },
  { emoji: '📚', text: 'Tìm khóa học', query: 'Có khóa học nào về React không?' },
  { emoji: '💰', text: 'Chính sách lương', query: 'Khi nào tôi nhận lương?' },
  { emoji: '📊', text: 'Performance Review', query: 'Quy trình đánh giá hiệu suất?' }
]

const SuggestionButton = React.memo(({ emoji, text, onClick }) => (
  <button className="suggestion-btn" onClick={onClick}>
    {emoji} {text}
  </button>
))

SuggestionButton.displayName = 'SuggestionButton'

const WelcomeScreen = React.memo(({ greetingMessage, onSuggestionClick }) => {
  const formattedGreeting = useMemo(
    () => formatMessage(greetingMessage),
    [greetingMessage]
  )

  return (
    <div className="welcome-screen">
      <div className="welcome-content">
        <div
          className="greeting-message"
          dangerouslySetInnerHTML={{ __html: formattedGreeting }}
        />
        <p className="help-text">Em có thể hỗ trợ bạn:</p>
        <div className="suggestions">
          {SUGGESTION_BUTTONS.map((btn, index) => (
            <SuggestionButton
              key={index}
              emoji={btn.emoji}
              text={btn.text}
              onClick={() => onSuggestionClick(btn.query)}
            />
          ))}
        </div>
      </div>
    </div>
  )
})

WelcomeScreen.displayName = 'WelcomeScreen'

export default WelcomeScreen

