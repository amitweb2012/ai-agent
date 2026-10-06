# Installation Guide

Use Python 3.12+ and uv.

Install uv:

    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv --version

Install the project from the repository root:

    uv sync --extra dev
    cp .env.example .env

Install Ollama models:

    ollama pull qwen3:1.7b
    ollama pull nomic-embed-text

Verify:

    uv run pytest
    uv run ai-basic
    uv run ai-rag

The project uses uv to create and manage the virtual environment. Keep .env out of source control.