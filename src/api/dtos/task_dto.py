from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskDTO(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    is_complete: bool = False
    created_at: datetime = datetime.now()