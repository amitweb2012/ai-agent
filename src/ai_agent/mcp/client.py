from contextlib import asynccontextmanager

from fastmcp import Client

from .server import mcp


@asynccontextmanager
async def connect():
    """Connect to the local FastMCP server."""
    async with Client(mcp) as client:
        yield client


async def discover_tools(client: Client):
    """Retrieve the tools exposed by the MCP server."""
    return await client.list_tools()


async def execute_tool(client: Client, tool_name: str, arguments: dict | None = None):
    """Execute an MCP tool by name."""
    return await client.call_tool(tool_name, arguments or {})
