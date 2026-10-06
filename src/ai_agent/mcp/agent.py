import asyncio

from openai import OpenAI

from ..config import settings
from .client import connect, discover_tools, execute_tool


def build_tool_descriptions(tools) -> str:
    return "\n".join(f"- {tool.name}: {tool.description}" for tool in tools)


def planner(user_input: str, tools, client: OpenAI) -> str | None:
    """Ask the LLM to select one available MCP tool or NONE."""
    prompt = f"""You are an AI planner.

Available tools:
{build_tool_descriptions(tools)}

Select a tool only when needed. For normal conversation return NONE. Otherwise return only the exact tool name.

User request: {user_input}"""
    response = client.chat.completions.create(model=settings.model, messages=[{"role": "user", "content": prompt}])
    tool_name = (response.choices[0].message.content or "").strip()
    if tool_name.upper() == "NONE":
        return None
    available = {tool.name for tool in tools}
    if tool_name not in available:
        raise ValueError(f"Planner selected unavailable tool: {tool_name}")
    return tool_name


def generate_response(user_input: str, client: OpenAI, tool_result=None) -> str:
    prompt = f"User: {user_input}"
    if tool_result is not None:
        prompt += f"\nTool result: {tool_result}"
    response = client.chat.completions.create(model=settings.model, messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content or "The model returned an empty answer."


async def main_async() -> None:
    llm = OpenAI(base_url=settings.base_url, api_key=settings.api_key)
    async with connect() as client:
        tools = await discover_tools(client)
        print("Available MCP tools:", ", ".join(tool.name for tool in tools))
        while True:
            user_input = input("User: ").strip()
            if user_input.lower() == "exit":
                print("Goodbye!")
                return
            tool_name = planner(user_input, tools, llm)
            result = await execute_tool(client, tool_name) if tool_name else None
            print("AI:", generate_response(user_input, llm, result))


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
