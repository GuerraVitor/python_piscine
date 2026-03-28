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


class SensorStream(DataStream):
    """Specialized stream for processing environmental sensor data."""
    def __init__(self, stream_id: str) -> None:
        print("Initializing Sensor Stream...")
        super().__init__(stream_id)
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:

        if not isinstance(data_batch, list):
            return "Error: Invalid batch format."

        valid_items: List[str] = [
            item for item in data_batch if isinstance(item, str)
        ]

        print(f"Processing sensor batch: {valid_items}")
        total_readings: int = 0
        for _ in valid_items:
            total_readings += 1

        temp_strs: List[str] = [
            item.split(":")[1] for item in valid_items if "temp:" in item
        ]

        temp_sum: float = 0.0
        temp_count: int = 0

        for t_val in temp_strs:
            try:
                temp_sum += float(t_val)
                temp_count += 1
            except ValueError:
                continue

        avg_temp = temp_sum / temp_count if temp_count > 0 else 0.0

        return (
            f"Sensor Analysis: {total_readings} readings processed, "
            f"avg temp: {avg_temp:.1f}ºC\n"
        )


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    sensor_data: List[Any] = ["temp:22.5", "humidity:65",
                              "pressure:1013", "temp:25.5",
                              "temp:29.7"]
    print(sensor.process_batch(sensor_data))

if __name__ == "__main__":
    main()
