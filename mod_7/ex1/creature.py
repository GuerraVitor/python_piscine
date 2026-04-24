"""Module defining specialized creatures with unique capabilities."""
from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """Concrete healing creature (Base form)."""

    def __init__(self) -> None:
        """Initialize Sproutling."""
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        """Perform Sproutling's attack."""
        return "Sproutling uses Vine Whip!"

    def heal(self, target: str | None = None) -> str:
        """Heal Sproutling."""
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Concrete healing creature (Evolved form)."""

    def __init__(self) -> None:
        """Initialize Bloomelle."""
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        """Perform Bloomelle's attack."""
        return "Bloomelle uses Petal Dance!"

    def heal(self, target: str | None = None) -> str:
        """Heal Bloomelle and allies."""
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """Concrete transforming creature (Base form)."""

    def __init__(self) -> None:
        """Initialize Shiftling."""
        super().__init__("Shiftling", "Normal")
        self.is_transformed: bool = False

    def attack(self) -> str:
        """Perform Shiftling's attack based on its form."""
        if self.is_transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        """Transform Shiftling into its enhanced form."""
        self.is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        """Revert Shiftling to its normal form."""
        self.is_transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    """Concrete transforming creature (Evolved form)."""

    def __init__(self) -> None:
        """Initialize Morphagon."""
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_transformed: bool = False

    def attack(self) -> str:
        """Perform Morphagon's attack based on its form."""
        if self.is_transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        """Transform Morphagon into its battle form."""
        self.is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        """Revert Morphagon to its stable form."""
        self.is_transformed = False
        return "Morphagon stabilizes its form."
