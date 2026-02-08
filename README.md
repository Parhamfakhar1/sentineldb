### 📝 ۲. `README.md` — مستندات اولیه

```markdown
# SentinelDB

Lightweight knowledge graph from plain text notes.  
Extract hidden relationships between ideas — no external DB, no cloud, just your notes.

## Install (Local Development)

```bash
git clone https://github.com/your-username/sentineldb.git
cd sentineldb
pip install -e .
```

## Quick Start

```python
from sentineldb import SentinelDB

db = SentinelDB("./my_knowledge")
db.add_note("crypto", "Bitcoin is a decentralized digital currency based on blockchain.")
db.add_note("smart_contracts", "Ethereum uses blockchain for smart contracts.")

print(db.find_related("blockchain"))  # ['crypto', 'smart_contracts']
db.save()
```

## Features
- ✅ Zero external dependencies
- ✅ Works offline
- ✅ Stores everything in JSON (human-readable)
- ✅ Easy to extend with NLP/embeddings later
- ✅ Supports Persian & English (via simple tokenizer)

## Roadmap
- [ ] Add CLI (`sentinel add`, `sentinel search`)
- [ ] Support Obsidian vaults
- [ ] Semantic search with Sentence-BERT
- [ ] Graph visualization (Pyvis export)
```

---