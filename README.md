# 🤖 AI Agent

Production-oriented Python starter for building tool-using AI agents with a clean orchestration layer, FastAPI API, tests, and a roadmap toward RAG, MCP, LangGraph, memory, and production deployment.

## Architecture

```text
Client
  │
  ▼
FastAPI
  │
  ▼
Agent Orchestrator
  │
  ├── Tool Registry
  │     └── Calculator Tool
  │
  └── LLM / Decision Layer (extensible)
```

## Features

- Python-first AI agent architecture
- Tool registry and execution abstraction
- FastAPI interface
- Pydantic configuration
- Pytest test suite
- GitHub Actions CI
- `uv`-friendly development workflow
- Secure environment configuration
- Designed for incremental production hardening

## Project Structure

```text
ai-agent/
├── src/ai_agent/
│   ├── agent.py
│   ├── api.py
│   ├── config.py
│   └── tools/
│       ├── base.py
│       └── calculator.py
├── tests/
│   ├── test_agent.py
│   └── test_calculator.py
├── .github/workflows/ci.yml
├── .env.example
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12+
- uv

### Install

```bash
uv sync
```

### Run tests

```bash
uv run pytest
```

### Run the API

```bash
uv run uvicorn ai_agent.api:app --reload
```

Then open `http://127.0.0.1:8000/docs`.

## Roadmap

1. LLM provider abstraction and structured tool calling
2. Conversation memory
3. PostgreSQL persistence
4. RAG with embeddings and vector search
5. MCP tool integration
6. LangGraph-based durable orchestration
7. Agent evaluation and tracing
8. Docker and Kubernetes deployment
9. OpenTelemetry observability
10. AWS/Azure production deployment

## Why This Repository

The goal is to evolve a simple agent into an enterprise-oriented AI engineering platform while keeping every architectural step understandable, testable, and deployable.

## License

MIT
