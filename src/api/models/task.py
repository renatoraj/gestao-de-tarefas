class Task:
    def __init__(self, id, title, description, is_complete=False, created_at=None):
        self.id = id
        self.title = title
        self.description = description
        self.is_complete = is_complete
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": self.is_complete,
            "created_at": self.created_at
        }