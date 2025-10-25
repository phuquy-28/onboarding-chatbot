# Frontend - Employee Onboarding Chatbot

React frontend with modern, modular architecture for the Employee Onboarding Chatbot.

## 🚀 Quick Setup

1. **Install dependencies:**
```bash
cd frontend
npm install
```

2. **Run the development server:**
```bash
npm run dev
```

The app will start on `http://localhost:5173`

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/         # UI Components
│   │   ├── ChatHeader.jsx          # Header with clear button
│   │   ├── WelcomeScreen.jsx       # Greeting + 12 suggestion buttons
│   │   ├── MessageList.jsx         # Message list with auto-scroll
│   │   ├── Message.jsx             # Single message display
│   │   ├── SuggestionChips.jsx     # Contextual suggestion chips
│   │   ├── TypingIndicator.jsx     # Loading animation
│   │   └── ChatInput.jsx           # Input area with send button
│   ├── hooks/              # Custom React Hooks
│   │   ├── useChat.js              # Chat state & message logic
│   │   └── useGreeting.js          # Greeting state & fetching
│   ├── services/           # API Layer
│   │   └── chatService.js          # API calls abstraction
│   ├── utils/              # Utility Functions
│   │   └── messageFormatter.js     # Markdown to HTML conversion
│   ├── App.jsx             # Main orchestrator
│   ├── App.css             # Styles
│   ├── main.jsx            # React entry point
│   └── index.css           # Global styles
├── package.json
├── vite.config.js
└── README.md              # This file
```

## ✨ Features

### 1. Modern Chat UI
- **Beautiful Design**: Gradient background with clean white chat interface
- **Smooth Animations**: Fade-in effects and typing indicators
- **Responsive Layout**: Works on desktop and mobile devices
- **Auto-scroll**: Automatically scrolls to latest message

### 2. Proactive Experience
- **Smart Greeting**: Auto-loads personalized greeting with urgent task alerts
- **Welcome Screen**: 12 static suggestion buttons for quick access
- **Contextual Chips**: 3 AI-generated suggestions after each bot response

### 3. Rich Formatting
- **Markdown Support**: Bold text, line breaks, lists
- **Emoji Indicators**: Visual cues for tasks, contacts, status
- **Structured Responses**: Well-organized information display

### 4. Performance Optimized
- **React.memo**: All components memoized to prevent unnecessary re-renders
- **useMemo**: Expensive computations cached
- **useCallback**: Functions memoized for referential equality
- **Component Splitting**: Small, focused components for better optimization

### 5. Real-time Messaging
- **Instant Communication**: Fast response from backend API
- **Typing Indicators**: Visual feedback when bot is processing
- **Error Handling**: Graceful error messages and connection error handling

### 6. Multi-turn Support
- **Conversation History**: Maintains full context across turns
- **Contextual Suggestions**: AI-generated follow-up prompts guide the conversation
- **Clear Conversation**: Reset chat with one click

## 🔧 Configuration

### API Connection

The frontend connects to the backend API at `http://localhost:5000/api` by default.

To change this, edit `API_URL` in `src/services/chatService.js`:

```javascript
const API_URL = 'http://localhost:5000/api'
```

### Default Employee

The system uses employee ID `E123` by default. To change this, edit `DEFAULT_EMPLOYEE_ID` in `src/services/chatService.js`.

## 💡 Usage

1. Make sure the backend is running on `http://localhost:5000`
2. Start the frontend development server
3. Open `http://localhost:5173` in your browser
4. Try the suggested questions or type your own!

## 🎯 Sample Questions

### Quick Start (Suggestion Buttons)
- 📋 Nhiệm vụ của tôi là gì?
- 👥 Ai là buddy của tôi?
- 💰 Khi nào tôi nhận lương?
- 💬 Kết nối với buddy
- ✅ Đánh dấu task hoàn thành
- ⏰ Kiểm tra deadline
- 📅 Lịch họp team
- 📶 Hỗ trợ IT
- 🏖️ Số dư phép
- 📚 Tìm khóa học
- 💰 Chính sách lương
- 📊 Performance Review

### Task Management
- "Nhiệm vụ của tôi là gì?"
- "Tôi đã hoàn thành khóa học Security"
- "Có nhiệm vụ nào sắp hết hạn không?"
- "Nhiệm vụ tiếp theo của tôi là gì?"

### Team & People
- "Team của tôi có lịch họp gì?"
- "Ai là team lead?"
- "Khi nào có meeting?"

### HR & IT
- "Tôi còn bao nhiêu ngày phép?"
- "Có khóa học nào về React không?"
- "Không vào được wifi F-town 3"
- "Quy trình đánh giá hiệu suất?"

## 🚀 Build for Production

```bash
npm run build
```

This will create an optimized production build in the `dist/` folder.

### Preview Production Build

```bash
npm run preview
```

## 📚 Additional Resources

- **Main README**: `../README.md` - Project overview
- **Backend README**: `../backend/README.md` - Backend documentation
- **REFACTORING.md**: `../REFACTORING.md` - Detailed refactoring guide
- **Memory Bank**: `../memory-bank/` - Complete project context

## 🐛 Troubleshooting

### Backend Connection Error
- Make sure backend is running on `http://localhost:5000`
- Check CORS configuration in backend
- Verify API_URL in `src/services/chatService.js`

### Build Errors
- Delete `node_modules` and run `npm install` again
- Clear Vite cache: `rm -rf node_modules/.vite`
- Check Node.js version (requires 18+)