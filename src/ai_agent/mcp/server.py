from datetime import datetime
import random
import secrets
import string

from fastmcp import FastMCP

mcp = FastMCP("AI Agent Time and Utility Server")


@mcp.tool()
def current_time() -> str:
    """Return the current date and time."""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


@mcp.tool()
def roll_dice() -> int:
    """Roll a six-sided die."""
    return random.randint(1, 6)


@mcp.tool()
def generate_password(length: int = 12) -> str:
    """Generate a secure random password."""
    if length < 4 or length > 256:
        raise ValueError("Password length must be between 4 and 256")
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main() -> None:
    print("Starting MCP server...")
    mcp.run()


if __name__ == "__main__":
    main()
