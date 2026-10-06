# AI Agent

A practical Python AI Agent learning project based on the original local **AI-AGENT** implementation. It demonstrates **Ollama/OpenAI-compatible LLMs, deterministic tools, embeddings, cosine similarity, RAG, and Model Context Protocol (MCP)**.

## Modules

| Module | Purpose |
|---|---|
| `basic` | Introductory assistant, personas, prompts, and deterministic tools |
| `rag` | Embeddings, cosine similarity, retrieval, grounded generation |
| `mcp` | FastMCP server/client and LLM-based tool selection |

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/) for the default local setup

Pull the example models:

```bash
ollama pull qwen3:1.7b
ollama pull nomic-embed-text
```

## Installation

```bash
git clone https://github.com/amitweb2012/ai-agent.git
cd ai-agent
uv sync --extra dev
cp .env.example .env
```

Default configuration:

```env
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL=qwen3:1.7b
EMBEDDING_MODEL=nomic-embed-text
RAG_MIN_SIMILARITY=0.5
```

Never commit a real `.env` or API keys.

## Run

### Basic assistant

```bash
uv run ai-basic
```

Choose Teacher, Python Expert, Travel Guide, Motivational Coach, or Interviewer.

Tool examples:

```text
What time is it?
Roll a dice
Generate a password
Explain notes.txt
Summarize project.txt
```

### Simple LLM call

```bash
uv run python -m ai_agent.basic.hello
```

### RAG assistant

```bash
uv run ai-rag
```

Flow:

```text
Question → embedding → cosine similarity → best document
         → threshold → LLM + context → grounded answer
```

Knowledge files live in `src/ai_agent/rag/knowledge/`.

### MCP server and agent

Terminal 1:

```bash
uv run ai-mcp-server
```

Terminal 2:

```bash
uv run ai-mcp-agent
```

The MCP server exposes `current_time`, `roll_dice`, and `generate_password`.

## Testing

```bash
uv run pytest
```

## Project structure

```text
ai-agent/
├── README.md
├── pyproject.toml
├── .env.example
├── docs/
├── src/
│   └── ai_agent/
│       ├── basic/
│       ├── data/
│       ├── mcp/
│       └── rag/
└── tests/
```

## Architecture

```text
User → AI Agent
          ├── Local Tools
          ├── RAG → Embeddings → Similarity → Knowledge
          └── MCP → Client → Server → Tools
                    │
                    ▼
             OpenAI-compatible LLM
                 (Ollama)
```

## Configuration

The OpenAI Python SDK is used against an OpenAI-compatible endpoint, so Ollama can be replaced by another compatible provider:

```env
BASE_URL=https://provider.example/v1
API_KEY=your-key
MODEL=your-model
EMBEDDING_MODEL=your-embedding-model
```

## Troubleshooting

**Connection refused on port 11434:** start Ollama and run `ollama list`.

**Model not found:**
```bash
ollama pull qwen3:1.7b
```

**Embedding model not found:**
```bash
ollama pull nomic-embed-text
```

**Import errors:** run commands from the repository root through `uv`, for example `uv run ai-rag`.

## Production evolution

The current project is intentionally educational, with clean boundaries for future:

- structured function/tool calling
- persistent memory
- PostgreSQL + pgvector
- chunking, reranking and citations
- MCP resources/prompts
- LangGraph
- Redis
- OpenTelemetry and Prometheus/Grafana
- OAuth2/OIDC/JWT/RBAC
- Docker hardening
- Kubernetes/Helm
- AWS EKS / Azure AKS

See the [documentation](docs/installation.md) and [roadmap](docs/roadmap.md).

## License

MIT
