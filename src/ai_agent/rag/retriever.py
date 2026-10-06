from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).resolve().parent / "knowledge"


def load_documents() -> dict[str, str]:
    """Load UTF-8 text documents from the knowledge directory."""
    return {path.name: path.read_text(encoding="utf-8") for path in KNOWLEDGE_DIR.glob("*.txt")}


def retrieve(question: str) -> tuple[str | None, str | None]:
    """Return the first document containing the full question text."""
    query = question.lower().strip()
    for filename, content in load_documents().items():
        if query and query in content.lower():
            return filename, content
    return None, None
