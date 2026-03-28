from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str
        """Process data and return result string."""
        DataProcessor
    @abstractmethod 
    def validate(self, data: Any) -> bool
    """Validade if data is appropriate for this processor."""

    def format_ouput(self, result: str) -> str
    """Format the output string."""
    return (f"Ouput: {result}")

class NumericProcessor(DataProcessor):
    """Specialized processor for list with numeric values."""

    def validate(self, data: Any) -> bool
    """Validate if data is a list of numbers."""
    
    def process(self, data: Any) -> str:
        """Calculate sum and average for a list of numbers."""

