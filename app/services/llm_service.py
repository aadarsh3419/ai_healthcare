import google.generativeai as genai
from app.core.config import settings
import os

os.environ["GOOGLE_API_KEY"] = settings.GEMINI_API_KEY
genai.configure(api_key=settings.GEMINI_API_KEY)

class LLMService:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")
    
    async def get_response(
        self,
        user_message: str,
        context: str,
        chat_history: list = []
    ) -> str:
        
        system_prompt = f"""Tu SwasthyaBot hai — ek helpful AI health assistant.
Tu Hindi aur English dono mein baat karta hai.

HEALTH KNOWLEDGE:
{context}

RULES:
- Sirf health topics pe baat karo
- Koi bhi disease definitively diagnose mat karo
- Emergency mein 112 call karne kaho
- Har jawab ke end mein doctor se milne ki salah do
"""
        history = []
        for msg in chat_history[-6:]:
            history.append({
                "role": msg["role"],
                "parts": [msg["content"]]
            })
        
        chat = self.model.start_chat(history=history)
        full_message = f"{system_prompt}\n\nUser: {user_message}"
        response = chat.send_message(full_message)
        return response.text

llm_service = LLMService()