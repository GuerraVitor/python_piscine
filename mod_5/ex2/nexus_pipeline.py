"""Provide polymorphic data processing pupeline."""

from abc import ABC, abstractmethod
from typing import Any, Dict, Union, Protocol, Deque
from collections import deque


class ProcessingStage(Protocol):
    """Protocol for processing stages."""

    def process(self, data: Any) -> Any:
        """Process data and return result."""
        ...
