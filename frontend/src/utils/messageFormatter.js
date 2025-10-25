/**
 * Message Formatter - Handles markdown and text formatting
 */

/**
 * Format message content with basic Markdown support
 * @param {string} content - Raw message content
 * @returns {string} Formatted HTML string
 */
export const formatMessage = (content) => {
  if (!content) return ''
  
  // Convert **bold** to <strong>
  let formatted = content.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
  
  // Convert line breaks
  formatted = formatted.replace(/\n/g, '<br/>')
  
  // Convert emoji lists (simple prefix check)
  formatted = formatted.replace(/^([✅⏳🔴🟡🟢📧📞💬⚠️📋📅📶🏖️📚💰📊])/gm, '$1')
  
  return formatted
}

