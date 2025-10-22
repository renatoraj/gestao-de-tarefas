from pydantic import BaseModel, Field
from typing import Optional

class TaskSchema(BaseModel):
    id: str
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    is_complete: bool = False
    created_at: str

    class Config:
        orm_mode = True