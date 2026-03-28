"""Provide advanced polymorphic data stream architecture."""


from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class defining core streaming functionality."""

    def __init__(self, stream_id: str) -> None:
        """Initialize stream with identifier."""
        self.stream_id: str = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(
            self, data_batch: List[Any], criteria: Optional[str] = None
            ) -> List[Any]:
        """Filter data based on criteria."""
        if criteria is None:
            return data_batch

        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""

        return {
            "stream_id": self.stream_id,
            "status": "active"
        }
