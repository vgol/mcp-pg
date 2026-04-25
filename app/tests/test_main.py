"""Tests for the mcp-pg server tools."""

from app.main import add, echo


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_echo() -> None:
    assert echo("hello") == "hello"
    assert echo("") == ""
