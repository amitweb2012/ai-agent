from collections import defaultdict

class InMemoryConversationStore:
    """Simple memory abstraction; replace the implementation with PostgreSQL/Redis later."""

    def __init__(self) -> None:
        self._messages: dict[str, list[dict[str, str]]] = defaultdict(list)

    def add(self, session_id: str, role: str, content: str) -> None:
        self._messages[session_id].append({"role": role, "content": content})

    def history(self, session_id: str) -> list[dict[str, str]]:
        return list(self._messages[session_id])

    def clear(self, session_id: str) -> None:
        self._messages.pop(session_id, None)
