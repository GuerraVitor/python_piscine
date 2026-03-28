from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data and return result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validade if data is appropriate for this processor."""
        pass

    def format_ouput(self, result: str) -> str:
        """Format the output string."""
        return f"Ouput: {result}"


class NumericProcessor(DataProcessor):
    """Specialized processor for list with numeric values."""

    def validate(self, data: Any) -> bool:
        """Validate if data is a list of numbers."""
        try:
            _ = data + []

            count: int = 0
            for i in data:
                float(i)
                count += 1

            return count > 0

        except (TypeError, ValueError):
            return False

    def process(self, data: Any) -> str:
        """Calculate sum and average for a list of numbers."""
