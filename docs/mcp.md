# Model Context Protocol

MCP provides a standard way for an AI application to discover and invoke tools exposed by another process or service.

Flow:

    Agent / LLM planner -> MCP Client -> MCP Server -> tools

Run the server:

    uv run ai-mcp-server

Run the agent in another terminal:

    uv run ai-mcp-agent

The current example uses an LLM planner that returns a tool name. A production version should use structured function/tool calling and validated arguments.