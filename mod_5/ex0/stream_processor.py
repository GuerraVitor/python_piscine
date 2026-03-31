"""Provide polymorphic data stream processing architecture."""

from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):
    """Abstract base class for all processors."""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate data."""
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data."""
        pass

    def format_output(self, result: str) -> str:
        """Formmated standard output."""
        return f"Output: {result}"


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
        return super().format_output(result)


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


def main() -> None:
    """Demonstrate polymorphic behavior of the Nexus processors."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    print("\nInitializing Numeric Processor...")
    num_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    if num_proc.validate(num_data):
        print("Validation: Numeric data verified")
        print(num_proc.process(num_data))

    print("\nInitializing Text Processor...")
    text_data: str = "Hello Nexus World"
    print(f"Processing data: \"{text_data}\"")
    if text_proc.validate(text_data):
        print("Validation: Text data verified")
        print(text_proc.process(text_data))

    print("\nInitializing Log Processor...")
    log_data: str = "ERROR: Connection timeout"
    print(f"Processing data: \"{log_data}\"")
    if log_proc.validate(log_data):
        print("Validation: Log entry verified")
        print(log_proc.process(log_data))

    print("\n=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")

    mixed_data: List[Any] = [[1, 2, 3], "Code Nexus", "INFO: System ready"]
    processors: List[DataProcessor] = [num_proc, text_proc, log_proc]

    count_id: int = 1
    for i in [0, 1, 2]:
        raw_res: str = processors[i].process(mixed_data[i])
        clean_res: str = raw_res.replace("Output: ", "")

        print(f"Result {count_id}: {clean_res}")
        count_id += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
