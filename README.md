# 🤖 Enterprise AI Agent

A production-oriented Python AI agent platform designed to evolve from a deterministic tool-using agent into an enterprise-grade **Agentic AI** system with LLM tool calling, memory, RAG, MCP, observability, and cloud-native deployment.

## Architecture

```text
                         ┌──────────────────┐
                         │ Web / API Client │
                         └────────┬─────────┘
                                  │
                           ┌──────▼──────┐
                           │ API Gateway │
                           └──────┬──────┘
                                  │
                     ┌────────────▼────────────┐
                     │      Agent Service      │
                     │  orchestration + state  │
                     └─────┬──────┬──────┬─────┘
                           │      │      │
                    ┌──────▼─┐ ┌──▼───┐ ┌▼──────────┐
                    │  LLM   │ │Memory│ │ Tools/MCP │
                    │Provider│ │Store │ │ Registry  │
                    └──────┬─┘ └──┬───┘ └────┬─────┘
                           │      │            │
                     ┌─────▼──────▼────────────▼─────┐
                     │ RAG / Vector DB / External    │
                     │ Systems / Observability      │
                     └───────────────────────────────┘
```

## Current Capabilities

- **Agent orchestration** with clean provider boundaries
- **Tool registry** with a safe calculator example
- **LLM provider abstraction** with deterministic local provider
- **Conversation memory** abstraction
- **RAG/retrieval** abstraction with local lexical retrieval
- **FastAPI** REST API and Swagger/OpenAPI
- **Pydantic** configuration and request models
- **Pytest** automated tests
- **Docker + Docker Compose**
- **GitHub Actions CI**
- **uv** development workflow

## Project Structure

```text
ai-agent/
├── .github/workflows/ci.yml
├── docs/
│   ├── architecture.md
│   └── roadmap.md
├── src/ai_agent/
│   ├── agent.py
│   ├── api.py
│   ├── config.py
│   ├── llm.py
│   ├── memory.py
│   ├── models.py
│   ├── rag.py
│   └── tools/
│       ├── base.py
│       └── calculator.py
├── tests/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Quick Start

### Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Docker (optional)

### Local

```bash
uv sync
uv run pytest
uv run uvicorn ai_agent.api:app --reload
```

Open **http://127.0.0.1:8000/docs**.

### Chat

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H 'content-type: application/json' \
  -d '{"session_id":"demo","message":"Explain AI agents"}'
```

### Calculator Tool

```bash
curl -X POST http://127.0.0.1:8000/tools/calculate \
  -H 'content-type: application/json' \
  -d '{"expression":"(10 + 5) * 2"}'
```

### Docker

```bash
docker compose up --build
```

## Engineering Principles

1. **Separation of concerns** — orchestration should not depend directly on infrastructure.
2. **Provider abstraction** — LLM, memory, retrieval, and tools can be replaced independently.
3. **Testability** — deterministic components make local development and CI reliable.
4. **Security by default** — secrets belong in environment/secret stores, never source code.
5. **Production evolution** — add infrastructure only when the corresponding requirement exists.

## Production Roadmap

### Phase 1 — Agent Core
- [x] Tool abstraction
- [x] Memory abstraction
- [x] LLM provider abstraction
- [x] RAG/retrieval abstraction

### Phase 2 — Generative AI
- [ ] OpenAI-compatible LLM provider
- [ ] Structured function/tool calling
- [ ] Streaming responses
- [ ] Prompt versioning
- [ ] Token and latency metrics

### Phase 3 — Enterprise Knowledge
- [ ] PostgreSQL
- [ ] pgvector
- [ ] Document ingestion
- [ ] Chunking and embeddings
- [ ] Hybrid retrieval
- [ ] Citation-aware answers

### Phase 4 — Agent Platform
- [ ] MCP client/server integration
- [ ] LangGraph workflows
- [ ] Human-in-the-loop approvals
- [ ] Durable execution
- [ ] Agent evaluation datasets

### Phase 5 — Production
- [ ] Redis
- [ ] OpenTelemetry
- [ ] Prometheus/Grafana
- [ ] Docker hardening
- [ ] Kubernetes + Helm
- [ ] AWS EKS / Azure AKS
- [ ] OAuth2/OIDC/RBAC

## Why This Project?

This repository is intended as a practical **AI Engineering / Forward-Deployed AI Engineer portfolio project**. The architecture starts small but is designed to demonstrate the engineering decisions required to move from an LLM demo to a reliable enterprise agent platform.

## License

MIT
