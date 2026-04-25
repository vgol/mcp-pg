# MCP Learning Plan

A step-by-step guide to understanding the Model Context Protocol by implementing its features one at a time in this playground server.

The server lives in `app/main.py`; tests live in `app/tests/test_main.py`.

---

## Protocol feature map

| # | Category | Feature | Status |
|---|---|---|---|
| — | Tools | Basic tool (`add`, `echo`) | ✅ done |
| — | Resources | Basic static resource (`info://server`) | ✅ done |
| — | Prompts | Basic single-message prompt (`greeting`) | ✅ done |
| 1 | Tools | Tool with `Context` — logging + progress | ⬜ todo |
| 2 | Resources | Dynamic resource with URI template | ⬜ todo |
| 3 | Tools | Structured output (Pydantic model) | ⬜ todo |
| 4 | Prompts | Multi-message prompt (system + user turn) | ⬜ todo |
| 5 | Tools | Image content (`ImageContent`) | ⬜ todo |
| 6 | Server | Lifespan — startup/shutdown with shared state | ⬜ todo |
| 7 | Tools | Error handling — explicit `McpError` | ⬜ todo |
| 8 | Completions | Argument autocompletion for a prompt | ⬜ todo |
| 9 | Resources | Resource template listing | ⬜ todo |
| 10 | Sampling | Server-initiated LLM call via `ctx.sample()` | ⬜ todo |
| 11 | Elicitation | Server asks client for user input | ⬜ todo |
| 12 | Transport | Streamable-HTTP transport + CORS | ⬜ todo |
| 13 | Advanced | Pagination via low-level server | ⬜ todo |

---

## Step-by-step implementation guide

### Step 1 — Tool context: logging and progress

Add a `slow_count` tool that accepts `steps: int` and uses `ctx: Context` to call
`ctx.info()`, `ctx.report_progress()`, and `ctx.debug()` on each iteration.

**What you learn:** the `Context` injection pattern — the fundamental way a tool communicates
back to the client during execution.

**Test:** call the function directly and assert the return value; test progress callbacks via a
mock context.

---

### Step 2 — Dynamic resource with URI template

Add a `note://notes/{note_id}` resource template so the server serves parameterised URLs.

**What you learn:** the difference between a static resource URI and a URI template, and how MCP
clients discover and dereference templates.

**Test:** call the underlying function with different `note_id` values and verify the returned
strings.

---

### Step 3 — Structured tool output

Add a `parse_date` tool that returns a `DateInfo` Pydantic model (year, month, day, weekday).

**What you learn:** tools can declare a typed schema for their output (structured output), making
them machine-readable for downstream processing.

**Test:** assert the returned model fields are correct for a known input.

---

### Step 4 — Multi-message prompt

Add a `code_review` prompt that returns a list of `Message` objects — a system instruction plus a
user message built from parameters.

**What you learn:** prompts are not just strings but structured conversation starters with roles.

**Test:** check that the return value is a list of messages with the correct roles and content.

---

### Step 5 — Image content from a tool

Add a `color_swatch` tool that accepts a hex colour string and returns an `Image` object (a tiny
PNG generated with stdlib `struct`/`zlib` — no extra dependency needed).

**What you learn:** MCP content is typed (`TextContent`, `ImageContent`, `EmbeddedResource`) and
clients must handle each type.

**Test:** verify the returned object is an `Image` with the right MIME type.

---

### Step 6 — Server lifespan

Introduce an `@asynccontextmanager` lifespan that initialises a simple in-memory "database" (a
plain `dict`) on startup and tears it down on shutdown. Wire a `db_query` tool that reads from
`ctx.request_context.lifespan_context`.

**What you learn:** how shared state (DB connections, caches, etc.) is safely managed across
requests using the lifespan pattern.

**Test:** inject a mock lifespan context and assert the tool uses it.

---

### Step 7 — Explicit error handling

Add a `safe_divide` tool that raises `McpError` with `ErrorCode.INVALID_PARAMS` when the divisor
is zero.

**What you learn:** the difference between a tool returning `isError=True` content and a
protocol-level error raised via `McpError`.

**Test:** assert the right exception type and message are raised.

---

### Step 8 — Argument autocompletion

Add a `choose_language` prompt with a `provide_completion` callback that returns autocomplete
suggestions for the `language` parameter from a fixed list.

**What you learn:** the Completions feature — how a client IDE/UI offers tab-completion for prompt
arguments.

**Test:** call the completion handler and verify the suggestions.

---

### Step 9 — Resource template listing

Explicitly inspect the server's registered resource templates so a client calling
`resources/templates/list` receives the URI patterns.

**What you learn:** how servers advertise which dynamic URIs they handle.

**Test:** inspect the server's registered resource templates list.

---

### Step 10 — Sampling (server → LLM → server)

Add a `summarise` tool that calls `await ctx.sample(messages=[...])` to ask the connected LLM
client to run an inference and return the result.

**What you learn:** the inverse of normal flow — the server drives the model, not the other way
around.

**Test:** mock `ctx.sample` and verify the tool forwards and returns the result correctly.

---

### Step 11 — Elicitation (server asks client for user input)

Add a `confirm_action` tool that calls `await ctx.elicit(message="...", schema=...)` to request
structured input from the user through the client UI before proceeding.

**What you learn:** interactive workflows where a tool needs human confirmation mid-execution.

**Test:** mock the elicitation response and verify the tool branches correctly.

---

### Step 12 — Streamable-HTTP transport

Update `main()` to accept a `--transport` CLI argument (using `argparse`) so the server can run
with `stdio` (default) or `streamable-http`.

**What you learn:** MCP transport options and how to expose a server over HTTP for real deployments.

**How to run:**
```bash
# stdio (default)
uv run mcp-pg

# HTTP — then open MCP Inspector and connect to http://localhost:8000/mcp
uv run mcp-pg --transport http
```

**Test:** verify argument parsing selects the correct transport string.

---

### Step 13 — Pagination (advanced / low-level)

Add a large item catalogue (>100 entries) and implement cursor-based pagination using the
low-level `@server.list_resources()` handler with `nextCursor` tokens.

**What you learn:** how large collections are broken into pages; the low-level server API that
underlies FastMCP.

**Test:** call the handler with and without a cursor and verify the correct slice and cursor values.

---

## Running the quality gate

After every change, run all four commands and fix any issues before proceeding:

```bash
uv run ruff check --fix .   # lint (auto-fix safe issues)
uv run ruff format .         # format
uv run ty check .            # type-check
uv run pytest ./app/tests    # tests
```
