from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SessionCreate(BaseModel):
    user_id: str

class SessionInDB(BaseModel):
    user_id: str
    session_id:str
    started_at: datetime
    ended_at:Optional[datetime] = None
    summary:Optional[str] = None
    key_symptoms:list[str] = []
    message_count:int = 0
    is_active: bool = True

class SessionResponse(BaseModel):
    session_id: str
    started_at: datetime
    ended_at: Optional[datetime] = None
    summary:Optional[str] = None
    key_symptoms: list[str] = []
    message_count:int 