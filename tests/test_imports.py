"""Smoke tests for the ReFly package."""

from refly import __version__
from refly.agents import BaseAgent
from refly.envs import BaseEnvironment


def test_package_exports_version() -> None:
    assert __version__ == "0.1.0"


def test_core_interfaces_are_importable() -> None:
    assert BaseAgent.__name__ == "BaseAgent"
    assert BaseEnvironment.__name__ == "BaseEnvironment"
