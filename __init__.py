"""
SentinelDB: Lightweight knowledge graph from plain text notes.
"""

from .core.graph import SentinelGraph
from .core.note import Note

class SentinelDB:
    def __init__(self, storage_path: str = "./sentinel_data"):
        self.graph = SentinelGraph(storage_path=storage_path)

    def add_note(self, note_id: str, content: str, metadata: dict = None):
        """Add a note and extract basic relationships."""
        note = Note(note_id=note_id, content=content, metadata=metadata or {})
        self.graph.add_note(note)

    def find_related(self, query: str, top_k: int = 5):
        """Find notes/entities related to the query."""
        return self.graph.find_related(query, top_k=top_k)

    def save(self):
        """Persist graph and notes to disk."""
        self.graph.save()

    def load(self):
        """Load existing data from disk."""
        self.graph.load()