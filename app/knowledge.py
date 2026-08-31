from pathlib import Path


KNOWLEDGE_FILE = Path("data/section8_basics.md")


def load_knowledge() -> str:
    return KNOWLEDGE_FILE.read_text(encoding="utf-8")