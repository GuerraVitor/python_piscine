"""Provide polymorphic data processing pupeline."""

from abc import ABC, abstractmethod
from typing import Any, Dict, Union, Protocol, Deque
from collections import deque


class ProcessingStage(Protocol):
    """Protocol for processing stages."""

    def process(self, data: Any) -> Any:
        """Process data and return result."""
        ...


class InputStage:
    """Stage 1: Input validation and parsing."""

    def process(self, data: Any) -> Any:
        """Validate the incoming data."""
        if isinstance(data, list):
            return [str(item).strip() for item in data]
        return data
