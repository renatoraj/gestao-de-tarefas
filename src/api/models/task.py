from datetime import datetime

class Task:
    def __init__(self, id: str, title: str, description: str = None, 
                 is_complete: bool = False, created_at: datetime = None):
        self.id = id
        self.title = title
        self.description = description
        self.is_complete = is_complete
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": self.is_complete,
            "created_at": self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at
        }