from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

@asynccontextmanager
async def lifespan(app:FastAPI):

    print(f"starting your health{settings.APP_NAME}...")
    yield

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
