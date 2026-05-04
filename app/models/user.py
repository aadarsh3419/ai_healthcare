from pydantic import BaseModel,EmailStr,Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):#this function is used to create the user schema for the request body while registering the user and it will be used in the auth.py file to perform the registration operation
    name: str
    email: EmailStr
    password: str
    phone: Optional[int] = None
    age: Optional[int] = None
    gender: Optional[str] = None

class UserLogin(BaseModel):#this function is used to create the user schema for the request body while logging in the user and it will be used in the auth.py file to perform the login operation 
    email: EmailStr
    password:str

class UserResponse(BaseModel):#this function is used to create the user response schema for the response body while registering and logging in the user and it will be used in the auh.py file to return the response after registration and login
    id:str
    name:str
    email:str
    phone:Optional[int]=None
    age:Optional[int]=None
    gender:Optional[str]=None
    created_at:datetime