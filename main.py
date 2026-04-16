from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import connect_db, disconnect_db

@asynccontextmanager
async def lifespan(app:FastAPI):

    await connect_db()

    print(f"starting your health{settings.APP_NAME}...")
    yield
    
    await disconnect_db()
    print("server shutting down")

app = FastAPI(
    title = settings.APP_NAME,
    debug=settings.DEBUG,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
async def root():
    return {"message":f"{settings.APP_NAME} is running"}
