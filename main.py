from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import connect_db, disconnect_db
from app.api.auth import router as auth_router

@asynccontextmanager
async def lifespan(app:FastAPI):#this function is used to manage the lifespan of the application and it will be used in the main.py file to run the application

    await connect_db()

    print(f"starting your health{settings.APP_NAME}...")
    yield
    
    await disconnect_db()
    print("server shutting down")

app = FastAPI(#this functionn is used to create the fastapi application and it will be used in the main.py file to run the application
    title = settings.APP_NAME,
    debug=settings.DEBUG,
    lifespan=lifespan
)

app.add_middleware(#this function is used to add the cors middleware to the application and it will be used in the main.py file to run the application
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])#this function is used to include the auth router in the application and it will be used in the main.py file to run the application

@app.get("/")#this function is used to create the root endpoint for the application and it will be used in the main.py file to run the application 
async def root():#this function is used  to crate the root endpoint for the application and it will be used in the main,py file to run the application 
    return {"message":f"{settings.APP_NAME} is running"}
