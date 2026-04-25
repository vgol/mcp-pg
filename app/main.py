"""Simple MCP server playground.

Demonstrates tools, resources, and prompts using the FastMCP API.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-pg")


# ── Tools ──────────────────────────────────────────────────────────────────────


@mcp.tool()
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


@mcp.tool()
def echo(message: str) -> str:
    """Return the message unchanged."""
    return message


# ── Resources ─────────────────────────────────────────────────────────────────


@mcp.resource("info://server")
def server_info() -> str:
    """Return basic information about this MCP server."""
    return "mcp-pg: a simple MCP server playground written in Python."


# ── Prompts ───────────────────────────────────────────────────────────────────


@mcp.prompt()
def greeting(name: str) -> str:
    """Generate a friendly greeting."""
    return f"Hello, {name}! Welcome to mcp-pg."


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
