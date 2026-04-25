# Copilot Instructions for mcp-pg

## Project Purpose

This is a **learning playground** for the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).
The goal is to understand how MCP works by building small, focused examples using the Python SDK.

## Stack

| Tool | Role |
|------|------|
| [uv](https://docs.astral.sh/uv/) | Python version management, virtual env, dependency management, and script runner |
| Python 3.13+ | Language (version pinned in `.python-version`, managed by `uv`) |
| [ruff](https://docs.astral.sh/ruff/) | Linting and formatting |
| [ty](https://github.com/astral-sh/ty) | Static type checking |
| [pytest](https://docs.pytest.org/) | Testing (tests live in `app/tests/`) |
| [FastMCP](https://github.com/modelcontextprotocol/python-sdk) | High-level MCP server API |

### Package management rules — strictly enforced

- **Only use `uv`** to manage dependencies and run tools.
- **Never use `pip`**, `pip install`, `uv pip install`, or any pip-based command.
- Add runtime dependencies: `uv add <package>`
- Add dev/test dependencies: `uv add --dev <package>`
- Run scripts and tools: `uv run <command>`

## Workflow for Every Change Request

Follow these four steps for every task, no matter how small:

### 1. Analyze
- Read the relevant source files and tests.
- Understand the current behaviour before proposing anything.

### 2. Plan
- Write a concise, step-by-step plan.
- Keep steps small and independently testable.

### 3. Implement (step by step)
- Make one small change at a time.
- After each step, run the quality gate (see below) before moving on.

### 4. Verify
- Confirm all quality-gate checks pass.
- Summarise what was changed and why.

## Quality Gate

Run all four commands after every change step and fix any issues before proceeding:

```bash
uv run ruff check --fix .   # lint (auto-fix safe issues)
uv run ruff format .         # format
uv run ty check .            # type-check
uv run pytest ./app/tests    # tests
```

All commands must exit with code `0` before a change is considered done.

## Project Layout

```
mcp-pg/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastMCP server — tools, resources, prompts
│   └── tests/
│       ├── __init__.py
│       └── test_main.py
├── pyproject.toml       # project metadata, ruff config, pytest config
├── uv.lock
└── .python-version
```

## Coding Conventions

- All public functions and methods must have docstrings.
- All function signatures must include type annotations (enforced by `ty`).
- Follow the existing file structure: tools, resources, and prompts are defined in `app/main.py` using the `@mcp.tool()`, `@mcp.resource()`, and `@mcp.prompt()` decorators.
- Tests go in `app/tests/` and must be discoverable by pytest without extra configuration.
- Prefer simple, readable code — this is a learning project, not production software.
