"""Base environment contract for ReFly."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseEnvironment(ABC):
    """Common interface for simulation-backed flight environments."""

    @abstractmethod
    def reset(self) -> Any:
        """Reset the environment and return the initial observation."""

    @abstractmethod
    def step(
        self, action: Any
    ) -> tuple[Any, float, bool, bool, dict[str, Any]]:
        """Advance the environment by one step."""
