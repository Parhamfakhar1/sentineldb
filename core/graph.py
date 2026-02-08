import os
import json
from collections import defaultdict
from typing import List, Dict, Set
from ..utils.nlp_helpers import extract_keywords

class SentinelGraph:
    def __init__(self, storage_path: str = "./sentinel_data"):
        self.storage_path = storage_path
        self.notes: Dict[str, Note] = {}
        self.entity_to_notes: Dict[str, Set[str]] = defaultdict(set)
        self._ensure_storage()

    def _ensure_storage(self):
        os.makedirs(self.storage_path, exist_ok=True)

    def add_note(self, note: "Note"):
        # Simple keyword extraction (can be upgraded to NER/embeddings later)
        keywords = extract_keywords(note.content)
        note.entities = keywords

        self.notes[note.note_id] = note

        # Build reverse index: entity -> note_ids
        for kw in keywords:
            self.entity_to_notes[kw].add(note.note_id)

    def find_related(self, query: str, top_k: int = 5) -> List[str]:
        query_keywords = extract_keywords(query)
        score = defaultdict(int)

        for kw in query_keywords:
            for note_id in self.entity_to_notes.get(kw, []):
                score[note_id] += 1

        # Sort by relevance (number of matching keywords)
        ranked = sorted(score.items(), key=lambda x: x[1], reverse=True)
        return [note_id for note_id, _ in ranked[:top_k]]

    def save(self):
        # Save notes
        notes_path = os.path.join(self.storage_path, "notes.json")
        serializable_notes = {
            nid: {
                "content": note.content,
                "metadata": note.metadata,
                "entities": list(note.entities)
            }
            for nid, note in self.notes.items()
        }
        with open(notes_path, "w", encoding="utf-8") as f:
            json.dump(serializable_notes, f, ensure_ascii=False, indent=2)

        # Save entity index
        index_path = os.path.join(self.storage_path, "index.json")
        serializable_index = {
            ent: list(note_ids)
            for ent, note_ids in self.entity_to_notes.items()
        }
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump(serializable_index, f, ensure_ascii=False, indent=2)

    def load(self):
        notes_path = os.path.join(self.storage_path, "notes.json")
        index_path = os.path.join(self.storage_path, "index.json")

        if os.path.exists(notes_path):
            with open(notes_path, "r", encoding="utf-8") as f:
                notes_data = json.load(f)
            for nid, data in notes_data.items():
                note = Note(nid, data["content"], data["metadata"])
                note.entities = set(data["entities"])
                self.notes[nid] = note

        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                index_data = json.load(f)
            self.entity_to_notes = defaultdict(set, {
                ent: set(note_ids) for ent, note_ids in index_data.items()
            })