# AI Agent

A practical Python AI Agent learning project based on the original local **AI-AGENT** implementation. It demonstrates **Ollama/OpenAI-compatible LLMs, deterministic tools, embeddings, RAG, and Model Context Protocol (MCP)**.

## Modules

| Module | Purpose |
|---|---|
| `basic` | Introductory assistant, personas, prompts, and deterministic tools |
| `rag` | Embeddings, similarity search, retrieval, grounded generation |
| `mcp` | MCP server/client and tool discovery |

## Prerequisites

- Python 3.12+
- uv
- Ollama for the default local setup

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

Example tool requests:

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

The MCP server exposes tools such as `current_time`, `roll_dice`, and `generate_password`.

## RAG and MCP — The Idea

**RAG (Retrieval-Augmented Generation)** and **MCP (Model Context Protocol)** solve different problems in an AI system.

### RAG

RAG is mainly about giving an LLM **relevant information from external knowledge** before it generates an answer.

```text
Question
   ↓
Create embedding
   ↓
Search relevant knowledge
   ↓
Retrieve context
   ↓
LLM + context
   ↓
Answer
```

For example, an enterprise assistant can retrieve information from company policies, documentation, manuals, or databases and use that information to answer a question.

**Think of RAG as:**

> "Find the right information and give it to the LLM."

### MCP

MCP is mainly about giving an AI application a **standard way to discover and use external tools and capabilities**.

```text
User request
     ↓
     LLM
     ↓
 MCP Client
     ↓
 MCP Server
     ↓
External Tool / System
     ↓
Tool Result
     ↓
     LLM
     ↓
   Answer
```

For example, an AI agent could use MCP tools to access a database, call an API, create a ticket, read files, or interact with another business system.

**Think of MCP as:**

> "Give the AI a standard way to use tools and systems."

### RAG vs MCP

| | RAG | MCP |
|---|---|---|
| Main purpose | Retrieve knowledge | Connect AI to tools/systems |
| Gives the AI | Information/context | Capabilities/actions |
| Typical use | Documents, policies, manuals, knowledge bases | APIs, databases, SaaS tools, files, business systems |
| Core idea | Search → retrieve → generate | Discover → call tool → receive result |
| Example | "What is our leave policy?" | "Create a leave request" |
| Usually read-oriented? | Yes | Can be read or write/action-oriented |

### They can work together

RAG and MCP are **not competing technologies**. A production AI agent may use both:

```text
                    AI Agent
                   /         \
                  /           \
                RAG           MCP
                 ↓             ↓
          Find knowledge    Use tools
                 ↓             ↓
             Context       Tool result
                  \           /
                   \         /
                      LLM
                       ↓
                    Answer
```

For example, an enterprise HR assistant could use **RAG** to retrieve the company's leave policy and **MCP** to call the HR system when the employee asks to submit a leave request.

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

## Configuration

The OpenAI Python SDK is used against an OpenAI-compatible endpoint, so Ollama can be replaced by another compatible provider:

```env
BASE_URL=https://provider.example/v1
API_KEY=your-key
MODEL=your-model
EMBEDDING_MODEL=your-embedding-model
```

## Troubleshooting

**Connection refused on port 11434:** start Ollama.

**Model not found:**
```bash
ollama pull qwen3:1.7b
```

**Embedding model not found:**
```bash
ollama pull nomic-embed-text
```

**Import errors:** run commands from the repository root through `uv`.

## License

MIT
