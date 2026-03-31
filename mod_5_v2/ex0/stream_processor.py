from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Abstract class base for model."""

    @abstractmethod
    def validade(self, data: Any) -> bool:
        """Validade data."""
        ...

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data."""
        ...

    def format_output(self, result: str) -> str:
        """Output result."""
        return f"Output {result}"


class NumericProcessor(DataProcessor):
    """Specialized numeric processor."""

    def validade(self, data: List[Any]) -> bool:
        """Validade if data is a List of int."""
        try:
            for cand in data:
                _ = float(cand)
            return True
        except (ValueError):
            print(f"Error: Input is not all numbers")
            return False

    def process(self, data: List[Any]) -> str:
        """Return the average and the sum for a list of numbers."""
        while not self.validade(data):
            user_input = input("Invalid input, try again: ")
            data = user_input.split()
        total = sum(float(i) for i in data)
        average = total / len(data)
        return (f"total: {total}, average: {average:.2f}")
