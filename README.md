# AI Healthcare Chatbot 🏥

An AI-powered healthcare chatbot that provides accurate health information in Hindi, Hinglish, and English using RAG (Retrieval-Augmented Generation).

## 🔍 Problem It Solves
LLMs can give outdated or incorrect health information. This chatbot uses RAG to ground responses in verified medical data — reducing hallucination and improving accuracy.

## ⚙️ Tech Stack
- **Python** — Backend
- **RAG** — Retrieval-Augmented Generation for accurate responses
- **LLM (Cohere)** — Language model integration
- **MongoDB** — Conversation history storage
- **JWT** — User authentication
- **Bcrypt** — Password hashing
- **FastAPI** — REST API

## ✨ Features
- Multilingual support — Hindi, Hinglish, English
- RAG-based responses using manually curated knowledge base
- 24-hour conversation history (auto-clears for privacy)
- Secure authentication with JWT
- Password hashing with Bcrypt

## 🚀 How to Run
1. Clone the repo
```bash
   git clone https://github.com/aadarsh3419/ai_healthcare.git
   cd ai_healthcare
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```
3. Create a `.env` file with your API keys
