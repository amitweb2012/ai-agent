# Architecture

## Enterprise Target

```text
Client → API Gateway → Agent Service
                         ├── LLM Provider
                         ├── Memory Store
                         ├── Tool Registry / MCP
                         ├── RAG / Vector DB
                         └── Observability
```

Provider and infrastructure boundaries are intentionally separated from orchestration so components can evolve independently.
