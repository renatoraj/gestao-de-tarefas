from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TaskCreateDTO(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)

class TaskUpdateDTO(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    is_complete: Optional[bool] = None

class TaskResponseDTO(BaseModel):
    id: str
    title: str
    description: Optional[str]
    is_complete: bool
    created_at: datetime
    
    class Config:
         orm_mode = True