from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Health Chatbot API"
    DEBUG: bool = False
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "healthchatbot"
    JWT_SECRET_KEY: str = "change_this_in_production"
    JWT_ALGORITHM: str = "HS256"
    GEMINI_API_KEY: str = ""
    CHROMA_DB_PATH: str = "./chroma_db"
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    TOP_K_RESULTS: int = 5

    class Config:
        env_file = ".env"

settings = Settings()  # ← yeh line ZAROORI hai