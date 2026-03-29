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


class TransformStage:
    def process(self, data: Any) -> Any:
        if data == "fail_sim":
            raise ValueError("Invalid data format")

        if isinstance(data, dict):
            return {str(i): str(j).upper() for i, j in data.items()}

        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        return data


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: Deque[ProcessingStage] = deque()

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass
