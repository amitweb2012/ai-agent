from typing import Any

from .tools.base import Tool
from .tools.calculator import CalculatorTool

class Agent:
    def __init__(self, tools: list[Tool] | None = None):
        self.tools = {tool.name: tool for tool in (tools or [CalculatorTool()])}

    def run(self, task: str, **kwargs: Any) -> Any:
        if task == "calculate":
            return self.tools["calculator"].execute(**kwargs).output
        raise ValueError(f"Unknown task: {task}")
