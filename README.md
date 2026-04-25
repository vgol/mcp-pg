# Project's name

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/badge/ruff-passing-brightgreen.svg?style=flat&logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![Mypy](https://img.shields.io/badge/mypy-passing-brightgreen.svg?style=flat&logo=python&logoColor=white)](http://mypy-lang.org/)
[![Coverage](https://img.shields.io/codecov/c/github/vgol/lazy-seller?flag=backend&logo=python&logoColor=white&label=backend%20coverage)](https://codecov.io/gh/vgol/lazy-seller)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.0%2B-3776AB.svg?style=flat&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

## uv commands

```bash
# aldredy done here
uv init

# unstall, pin managed Python's versoin
uv python list
uv python install <python-ver>

# add / remove packages
uv add / remove  <package>

# sync packages (with upgrade)
uv sync --all-groups --upgrade

# re-create venv
uv venv --clear

# run app ro tool

uv run <app>
uv tool install <tool>
uv tool run <tool>
```
