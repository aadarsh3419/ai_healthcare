# AI Health Chatbot

## Setup
1. pip install -r requirements.txt
2. .env file mein keys daalo
3. uvicorn main:app --reload --port 8000

## APIs
- POST /api/auth/register
- POST /api/auth/login
- POST /api/chat/send (Bearer token)
- GET  /api/chat/history (Bearer token)
