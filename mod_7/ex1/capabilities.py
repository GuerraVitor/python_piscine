"""Module defining capability interfaces for creatures."""
from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract interface for creatures that can heal."""

    @abstractmethod
    def heal(self, target: str | None = None) -> str:
        """Perform a healing action."""
        pass


class TransformCapability(ABC):
    """Abstract interface for creatures that can transform."""

    @abstractmethod
    def transform(self) -> str:
        """Transform the creature into an alternate state."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Revert the creature to its normal state."""
        pass
