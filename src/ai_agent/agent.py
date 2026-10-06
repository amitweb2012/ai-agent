from typing import Any

from .llm import LLMProvider, MockLLMProvider
from .memory import InMemoryConversationStore
from .rag import InMemoryRetriever
from .tools.base import Tool
from .tools.calculator import CalculatorTool

class Agent:
    def __init__(
        self,
        tools: list[Tool] | None = None,
        llm: LLMProvider | None = None,
        memory: InMemoryConversationStore | None = None,
        retriever: InMemoryRetriever | None = None,
    ):
        self.tools = {tool.name: tool for tool in (tools or [CalculatorTool()])}
        self.llm = llm or MockLLMProvider()
        self.memory = memory or InMemoryConversationStore()
        self.retriever = retriever or InMemoryRetriever()

    def run(self, task: str, **kwargs: Any) -> Any:
        if task == "calculate":
            return self.tools["calculator"].execute(**kwargs).output
        raise ValueError(f"Unknown task: {task}")

    def chat(self, session_id: str, message: str) -> tuple[str, list[str]]:
        self.memory.add(session_id, "user", message)
        context = self.retriever.search(message)
        messages = self.memory.history(session_id)
        if context:
            messages.append({
                "role": "system",
                "content": "Relevant knowledge:\n" + "\n".join(d.text for d in context),
            })
        response = self.llm.generate(messages)
        self.memory.add(session_id, "assistant", response)
        return response, []
