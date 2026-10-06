# Development Guide

Install development dependencies:

    uv sync --extra dev

Run tests:

    uv run pytest

Run a module:

    uv run python -m ai_agent.basic.hello

Keep deterministic tools separate from LLM calls, retrieval separate from generation, and MCP transport separate from planning. Add tests when adding tools or retrieval behavior. Never commit .env or secrets.

To add knowledge, place a UTF-8 .txt file under src/ai_agent/rag/knowledge/. The loader discovers it automatically.