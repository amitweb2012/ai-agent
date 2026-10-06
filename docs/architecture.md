# Architecture

The project has three learning layers:

1. Basic agent: prompt + deterministic tool routing + LLM.
2. RAG: document loading + embeddings + cosine similarity + grounded generation.
3. MCP: tool server + client discovery + LLM planner + tool execution.

High-level flow:

    User -> AI Agent
             |-> Local Tools
             |-> RAG -> embeddings -> similarity -> knowledge
             |-> MCP -> client -> server -> tools
             |
             +-> OpenAI-compatible LLM / Ollama

Production evolution can replace text files with PostgreSQL/pgvector, simple routing with structured tool calling, local CLI with FastAPI, local state with Redis/PostgreSQL, and add OpenTelemetry, OAuth2/OIDC/JWT/RBAC, Kubernetes and cloud deployment.