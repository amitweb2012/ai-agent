from dataclasses import dataclass

@dataclass(frozen=True)
class Document:
    id: str
    text: str
    metadata: dict[str, str]

class InMemoryRetriever:
    """RAG boundary with a simple lexical implementation for local development."""

    def __init__(self, documents: list[Document] | None = None):
        self.documents = documents or []

    def add(self, document: Document) -> None:
        self.documents.append(document)

    def search(self, query: str, top_k: int = 3) -> list[Document]:
        terms = set(query.lower().split())
        scored = []
        for doc in self.documents:
            score = sum(term in doc.text.lower() for term in terms)
            if score:
                scored.append((score, doc))
        return [doc for _, doc in sorted(scored, key=lambda item: item[0], reverse=True)[:top_k]]
