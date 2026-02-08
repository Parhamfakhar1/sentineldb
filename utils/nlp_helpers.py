import re
from typing import Set

def extract_keywords(text: str) -> Set[str]:
    """
    Very simple keyword extractor.
    - Lowercase
    - Remove punctuation
    - Keep words longer than 2 chars
    - Can be replaced later with NER or embeddings
    """
    # Basic cleaning
    text = re.sub(r"[^\w\s]", " ", text.lower())
    words = text.split()
    # Filter short words and common stop words (minimal list)
    stop_words = {"the", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by"}
    keywords = {word for word in words if len(word) > 2 and word not in stop_words}
    return keywords