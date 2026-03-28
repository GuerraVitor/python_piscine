from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

	@abstractmethod
	def process(self, data: Any) -> str
	"""Process data and return result string."""

	@abstractmethod
	def validate(self, data: Any) -> bool
	"""Validade if data is appropriate for this processor."""

	def format_ouput(self, result: str) -> str
	"""Format the output string."""
	return f"Ouput: {result}"
