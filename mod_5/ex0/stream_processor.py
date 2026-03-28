"""Provide polymorphic data stream processing architecture."""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    """Abstract base class defining the common processing interface."""

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
        """Validate numeric list using Duck Typing and try/except."""
        try:
            # Test if it behaves like a list by concatenating
            _ = data + []
            count: int = 0
            for item in data:
                float(item)
                count += 1
            return count > 0
        except (TypeError, ValueError):
            return False

    def process(self, data: Any) -> str:
        """Process numeric data calculating sum and average manually."""
        if not self.validate(data):
            return "Error: Invalid numeric data"

        total_sum: float = 0.0
        count: int = 0
        for item in data:
            total_sum += float(item)
            count += 1

        avg: float = total_sum / count if count > 0 else 0.0

        # Format sum to int if it's a whole number to match example output
        sum_val: Union[int, float] = (
            int(total_sum) if total_sum.is_integer() else total_sum
        )

        result: str = (
            f"Processed {count} numeric values, sum={sum_val}, avg={avg}"
        )
        return super().format_output(result)
