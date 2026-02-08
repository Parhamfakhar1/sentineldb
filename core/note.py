from typing import Dict, Any

class Note:
    def __init__(self, note_id: str, content: str, metadata: Dict[str, Any] = None):
        self.note_id = note_id
        self.content = content
        self.metadata = metadata or {}
        self.entities = set()  # Will be filled by extractor later

    def __repr__(self):
        return f"<Note id={self.note_id}>"