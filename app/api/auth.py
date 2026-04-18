from fastapi import APIRouter, HTTPException, status, Depends
from datetime import datetime, timezone
from app.core.database import get_db
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import UserCreate, UserLogin, UserResponse
router = APIRouter()

@router.post("/register")
async def register(user_data: UserCreate):
    db = get_db()

    existing_user = await db["users"].find_one(
        {"email": user_data.email}
    )
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email already exists"
        )
    hashed = hash_password(user_data.password)

    new_user = {
        "name": user_data.name,
        "email": user_data.email,
        "password": hashed,
        "phone":user_data.phone,
        "age": user_data.age,
        "gender": user_data.gender,
        "is_active": True,
        "created_at":datetime.now(timezone.utc)

    }

    result = await db["users"].insert_one(new_user)

    token = create_access_token({
        "user_id": str(result.inserted_id),
        "email":user_data.email
    })

    return {
        "message":"registration sussefull",
        "token": token,
        "user":{
            "id":str(result.inserted_id),
            "name":user_data.name,
            "email": user_data.email
        }
    }

@router.post("/login")
async def login(user_data: UserLogin):
    db = get_db()

    user = await db["users"].find_one(
        {"email":user_data.email}
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"

        )
    is_valid = verify_password(user_data.password,user["password"])
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    token = create_access_token({
        "user_id":str(user["_id"]),
        "email": user["email"]
    })
    return {
        "message": "Login successful",
        "token": token,
        "user": {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        }
    }

@router.get("/me")
async def get_me():
    return {"message": "coming soon"}
