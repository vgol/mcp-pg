# mcp-pg

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/badge/ruff-passing-brightgreen.svg?style=flat&logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/badge/ty-passing-brightgreen.svg?style=flat)](https://github.com/astral-sh/ty)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)

A minimal [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) server written in Python.  
The goal is to understand how MCP works by building a small playground server.

## Features

- **Tools** – `add` (sums two integers), `echo` (returns a message unchanged)
- **Resource** – `info://server` (returns a description of this server)
- **Prompt** – `greeting` (generates a friendly greeting)

## Stack

| Tool | Purpose |
|------|---------|
| [uv](https://docs.astral.sh/uv/) | Package & project management |
| [ruff](https://docs.astral.sh/ruff/) | Linter & formatter |
| [ty](https://github.com/astral-sh/ty) | Static type checker |
| [pytest](https://pytest.org) | Tests |
| [mcp](https://github.com/modelcontextprotocol/python-sdk) | MCP Python SDK |

## Quickstart

```bash
# Install dependencies
uv sync

# Run the MCP server (stdio transport, default)
uv run mcp-pg

# Inspect the server interactively with the MCP Inspector
uv run mcp dev app/main.py
```

## Development

```bash
# Lint & format
uv run ruff check .
uv run ruff format .

# Type-check
uv run ty check app

# Tests
uv run pytest
```

## uv cheat-sheet

```bash
# Install / pin a specific Python version
uv python install 3.13

# Add / remove a dependency
uv add <package>
uv remove <package>

# Add a dev-only dependency
uv add --dev <package>

# Sync (with upgrade)
uv sync --all-groups --upgrade

# Re-create the virtual environment
uv venv --clear

# Run a script or tool
uv run <script>
uv tool run <tool>
```

## MCP concepts

| Concept | Description |
|---------|-------------|
| **Tool** | A callable function exposed to the LLM (`@mcp.tool()`) |
| **Resource** | Read-only data the LLM can fetch (`@mcp.resource(uri)`) |
| **Prompt** | A reusable prompt template (`@mcp.prompt()`) |
