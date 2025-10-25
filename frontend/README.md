# Frontend - Employee Onboarding Chatbot

React frontend with modern chat UI for the Employee Onboarding Chatbot.

## Setup

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

## Features

- **Modern Chat UI**: Beautiful gradient design with smooth animations
- **Real-time Messaging**: Instant communication with backend API
- **Typing Indicators**: Visual feedback when bot is processing
- **Suggestion Buttons**: Quick access to common questions
- **Auto-scroll**: Automatically scrolls to latest message
- **Responsive Design**: Works on desktop and mobile devices
- **Multi-turn Support**: Maintains conversation context

## Project Structure

```
frontend/
├── src/
│   ├── App.jsx         # Main chat component
│   ├── App.css         # Chat UI styling
│   ├── main.jsx        # React entry point
│   └── index.css       # Global styles
├── package.json
└── vite.config.js
```

## Configuration

The frontend connects to the backend API at `http://localhost:5000/api` by default. If you need to change this, update the `API_URL` constant in `App.jsx`.

## Usage

1. Make sure the backend is running on `http://localhost:5000`
2. Start the frontend development server
3. Open `http://localhost:5173` in your browser
4. Try the suggested questions or type your own!

## Sample Questions

- "Khi nào tôi nhận lương?"
- "Nhiệm vụ của tôi là gì?"
- "Ai là quản lý của tôi?"
- "Làm sao để cài đặt email?"
- "Chính sách nghỉ phép như thế nào?"

## Build for Production

```bash
npm run build
```

This will create an optimized production build in the `dist/` folder.
