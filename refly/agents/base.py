"""Base agent contract for ReFly."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseAgent(ABC):
    """Common interface for flight agents."""

    @abstractmethod
    def reset(self) -> None:
        """Reset any internal state before a new episode starts."""

    @abstractmethod
    def act(self, observation: Any) -> Any:
        """Return an action for the given observation."""

    @abstractmethod
    def save(self, path: str) -> None:
        """Persist the agent state."""

    @abstractmethod
    def load(self, path: str) -> None:
        """Restore the agent state."""
