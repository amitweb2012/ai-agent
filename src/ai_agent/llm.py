from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    def generate(self, messages: list[dict[str, str]]) -> str:
        raise NotImplementedError

class MockLLMProvider(LLMProvider):
    """Deterministic provider used for local development and tests."""

    def generate(self, messages: list[dict[str, str]]) -> str:
        last = messages[-1]["content"]
        return f"Agent received: {last}"
