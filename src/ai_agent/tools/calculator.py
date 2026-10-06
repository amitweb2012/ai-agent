import ast
import operator
from typing import Any

from .base import Tool, ToolResult

_ALLOWED = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

class CalculatorTool(Tool):
    name = "calculator"

    def execute(self, expression: str) -> ToolResult:
        tree = ast.parse(expression, mode="eval")
        value = self._eval(tree.body)
        return ToolResult(output=value)

    def _eval(self, node: ast.AST) -> Any:
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED:
            return _ALLOWED[type(node.op)](self._eval(node.operand))
        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
            return _ALLOWED[type(node.op)](self._eval(node.left), self._eval(node.right))
        raise ValueError("Unsupported expression")
