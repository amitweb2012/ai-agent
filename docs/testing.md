# Testing

The repository includes tests for deterministic tools, tool routing, cosine similarity, and knowledge loading.

Run:

    uv run pytest

The tests are intentionally offline for the core utilities. LLM-dependent examples require Ollama or another configured OpenAI-compatible endpoint.
