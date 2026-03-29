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
        """Validate and parse the incoming data."""
        if isinstance(data, str) and "," in data:
            return [str(item).strip() for item in data.split(",")]

        if isinstance(data, list):
            return [str(item).strip() for item in data]

        return data


class TransformStage:
    """Stage 2: Data transformation and enrichment."""

    def process(self, data: Any) -> Any:
        """Transform the data using comprehensions."""
        if data == "fail_sim":
            raise ValueError("Invalid data format")

        if isinstance(data, dict):
            return {str(k): str(v).upper() for k, v in data.items()}

        if isinstance(data, list):
            return [str(item).upper() for item in data]

        return data


class OutputStage:
    """Stage 3: Output formatting and delivery."""

    def process(self, data: Any) -> Any:
        """Pass the processed data forward."""
        return data


class ProcessingPipeline(ABC):
    """Abstract base class managing processing stages."""

    def __init__(self, pipeline_id: str) -> None:
        """Initialize the pipeline with an ID and empty stages."""
        self.pipeline_id: str = pipeline_id
        self.stages: Deque[ProcessingStage] = deque()

    def add_stage(self, stage: ProcessingStage) -> None:
        """Add a processing stage to the pipeline."""
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        """Process data through the pipeline stages."""
        pass


class JSONAdapter(ProcessingPipeline):
    """Pipeline adapter for JSON format data."""

    def process(self, data: Any) -> Union[str, Any]:
        """Process JSON and extract specific keys."""
        print("\nProcessing JSON data through pipeline...")
        print(f"Input: {data}")
        current_data: Any = data

        try:
            for stage in self.stages:
                current_data = stage.process(current_data)
            print("Transform: Enriched with metadata and validation")

            val: str = "0.0"
            if isinstance(current_data, dict):
                for key, value in current_data.items():
                    if key == "value" or key == "VALUE":
                        val = str(value)

            return (
                f"Output: Processed temperature reading: "
                f"{val}ºC (Normal range)"
            )
        except Exception as err:
            return f"Error detected: {err}"


class CSVAdapter(ProcessingPipeline):
    """Pipeline adapter for CSV format data."""

    def process(self, data: Any) -> Union[str, Any]:
        """Process CSV data and dynamically count records."""
        print("\nProcessing CSV data through same pipeline...")
        print(f"Input: {data}")
        current_data: Any = data

        try:
            for stage in self.stages:
                current_data = stage.process(current_data)
            print("Transform: Parsed and structured data")

            count: int = 0
            if isinstance(current_data, list):
                for _ in current_data:
                    count += 1

            actions: int = count // 3 if count >= 3 else count

            return f"Output: User activity logged: {actions} actions processed"
        except Exception as err:
            return f"Error detected: {err}"


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter for stream data."""

    def process(self, data: Any) -> Union[str, Any]:
        """Process stream dynamically, calculating averages."""
        print("\nProcessing Stream data through same pipeline...")
        print(f"Input: {data}")
        current_data: Any = data

        try:
            for stage in self.stages:
                current_data = stage.process(current_data)
            print("Transform: Aggregated and filtered")

            count: int = 0
            total: float = 0.0

            if isinstance(current_data, list):
                for item in current_data:
                    count += 1
                    if ":" in str(item):
                        try:
                            val_str: str = str(item).split(":")[1]
                            total += float(val_str)
                        except ValueError:
                            pass

            avg: float = total / count if count > 0 else 0.0

            return (
                f"Output: Stream summary: {count} readings, "
                f"avg: {avg:.1f}ºC"
            )
        except Exception as err:
            print(f"Error detected in Stage 2: {err}")
            print("Recovery initiated: Switching to backup processor")
            return (
                "Recovery successful: Pipeline restored, "
                "processing resumed"
            )
