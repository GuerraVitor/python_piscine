"""Specialized creatures with healing and transform capabilities."""
from ex0.creature import Creature

from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """Base creature for the healing family."""

    def __init__(self) -> None:
        super().__init__("Sproutling", "Plant")

    def attack(self) -> str:
        return "Sproutling uses Leaf Bite!"

    def heal(self, target: str | None = None) -> str:
        if target is None:
            return "Sproutling heals itself."
        return f"Sproutling heals {target}."


class Bloomelle(Creature, HealCapability):
    """Evolved creature for the healing family."""

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Plant")

    def attack(self) -> str:
        return "Bloomelle uses Petal Burst!"

    def heal(self, target: str | None = None) -> str:
        if target is None:
            return "Bloomelle heals itself and nearby allies."
        return f"Bloomelle heals {target} and nearby allies."


class Shiftling(Creature, TransformCapability):
    """Base creature for the transform family."""

    def __init__(self) -> None:
        super().__init__("Shiftling", "Shadow")
        self.is_transformed: bool = False

    def attack(self) -> str:
        if self.is_transformed:
            return "Shiftling uses Phantom Slash!"
        return "Shiftling uses Shadow Tap!"

    def transform(self) -> str:
        self.is_transformed = True
        return "Shiftling shifts into its shadow form."

    def revert(self) -> str:
        self.is_transformed = False
        return "Shiftling returns to its normal form."


class Morphagon(Creature, TransformCapability):
    """Evolved creature for the transform family."""

    def __init__(self) -> None:
        super().__init__("Morphagon", "Shadow")
        self.is_transformed: bool = False

    def attack(self) -> str:
        if self.is_transformed:
            return "Morphagon uses Night Break!"
        return "Morphagon uses Echo Strike!"

    def transform(self) -> str:
        self.is_transformed = True
        return "Morphagon shifts into its battle form."

    def revert(self) -> str:
        self.is_transformed = False
        return "Morphagon returns to its original form."
