from typing import List, Dict, Any, Optional

class Conversation:
    """
    Simple model for conversation data.
    In a full implementation, this would be a SQLAlchemy model.
    """
    def __init__(
        self,
        id: Optional[str] = None,
        user_id: Optional[str] = None,
        messages: List[Dict[str, Any]] = None
    ):
        self.id = id
        self.user_id = user_id
        self.messages = messages or []
    
    def add_message(self, role: str, content: str):
        self.messages.append({
            "role": role,
            "content": content
        })
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "messages": self.messages
        }