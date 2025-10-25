/**
 * SuggestionChips Component - Displays contextual suggestion chips
 */

import React from 'react'

const SuggestionChip = React.memo(({ prompt, onClick, disabled }) => (
  <button
    className="suggestion-chip"
    onClick={() => onClick(prompt)}
    disabled={disabled}
  >
    {prompt}
  </button>
))

SuggestionChip.displayName = 'SuggestionChip'

const SuggestionChips = React.memo(({ prompts, onChipClick, disabled }) => {
  if (!prompts || prompts.length === 0) return null

  return (
    <div className="suggestion-chips">
      {prompts.map((prompt, index) => (
        <SuggestionChip
          key={index}
          prompt={prompt}
          onClick={onChipClick}
          disabled={disabled}
        />
      ))}
    </div>
  )
})

SuggestionChips.displayName = 'SuggestionChips'

export default SuggestionChips

