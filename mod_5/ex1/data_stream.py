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
        """Initialize the sensor stream and announce its creation."""
        super().__init__(stream_id)
        print("\nInitializing Sensor Stream...")
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
            f"avg temp: {avg_temp:.1f}ºC"
        )


class TransactionStream(DataStream):
    """Specialized stream for financial transaction."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the transaction stream and announce its creation."""
        super().__init__(stream_id)
        print("\nInitializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transactions calculating total operations and net flow."""
        if not isinstance(data_batch, list):
            return "Error: Invalid batch format."

        valid_items: List[str] = [
            item for item in data_batch if isinstance(item, str)
        ]
        print(f"Processing transaction batch: {valid_items}")

        operations_count: int = 0
        for _ in valid_items:
            operations_count += 1

        net_flow: float = 0.0

        for item in valid_items:
            try:
                if "buy" in item:
                    val: float = float(item.split(":")[1])
                    net_flow += val
                elif "sell" in item:
                    val: float = float(item.split(":")[1])
                    net_flow -= val
            except ValueError:
                continue

        flow_val: Union[int, float] = (
            int(net_flow) if net_flow.is_integer() else net_flow
        )
        sign: str = "+" if flow_val > 0 else ""

        return (
            f"Transaction analysis: {operations_count} operations, "
            f"net flow: {sign}{flow_val} units"
        )


class EventStream(DataStream):
    """Specialized stream for tracking system events and errors."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the event stream and announce its creation."""
        super().__init__(stream_id)
        print("\nInitializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process system events and count error occurrences."""
        if not isinstance(data_batch, list):
            return "Error: Invalid batch format."

        valid_events: List[str] = [
            item for item in data_batch if isinstance(item, str)
        ]
        print(f"Processing transaction batch: {valid_events}")

        total_events: int = 0
        for _ in valid_events:
            total_events += 1

        error_events: List[str] = [
            event for event in valid_events if "error" in event
        ]

        error_count: int = 0
        for _ in error_events:
            error_count += 1

        error_word: str = "error" if error_count == 1 else "errors"
        return (
            f"Event analysis: {total_events} events, "
            f"{error_count} {error_word} detected"
        )


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    sensor_data: List[Any] = ["temp:22.5", "humidity:65", "pressure:1013",]
    print(sensor.process_batch(sensor_data))

    trans = TransactionStream("TRANS_001")
    trans_data: List[Any] = ["buy:100", "sell:150", "buy:75"]
    print(trans.process_batch(trans_data))

    event = EventStream("EVENT_001")
    event_data: List[Any] = ["login", "error", "logout"]
    print(event.process_batch(event_data))


if __name__ == "__main__":
    main()
