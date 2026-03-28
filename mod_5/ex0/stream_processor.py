"""Provide polymorphic data stream processing architecture."""

from abc import ABC, abstractmethod
from typing import Any, List, Union


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


class TextProcessor(DataProcessor):
    """Specialized processor for text string."""

    def validate(self, data: Any) -> bool:
        """Validade if data is a string."""
        try:
            _ = data.upper()
            return True
        except AttributeError:
            return False

    def process(self, data: Any) -> str:
        """Process text data counting characters and words."""
        if not self.validate(data):
            return "Error: Invali text data"

        char_count: int = 0
        word_count: int = 0
        in_word: bool = False

        for char in data:
            char_count += 1
            if char != ' ' and not in_word:
                in_word = True
                word_count += 1
            elif char == ' ':
                in_word = False

        result: str = (
            f"Processed text: {char_count} characters, {word_count} words"
        )
        return super.format_output(result)


class LogProcessor(DataProcessor):
    """Specialized processor for log entries."""

    def validate(self, data: Any) -> bool:
        """Validate log string for specific archive tags."""
        try:
            _ = data.upper()
            if "ERROR:" in data or "INFO:" in data:
                return True
            return False
        except AttributeError:
            return False

    def process(self, data: Any) -> str:
        """Process log entries to identify severity levels."""
        if not self.validate(data):
            return "Error: Invalid log data"

        parts: List[str] = data.split(":", 1)
        level: str = parts[0]

        message: str = ""
        found: bool = False
        for p in parts:
            if found:
                message = p.strip()
            found = True

        prefix: str = "[ALERT]" if level == "ERROR" else "[INFO]"
        result: str = f"{prefix} {level} level detected: {message}"
        return super().format_output(result)
