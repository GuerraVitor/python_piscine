"""Module defining specialized creatures with unique capabilities."""
from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Oddish(Creature, HealCapability):
    """Concrete healing creature (Base form)."""

    def __init__(self) -> None:
        """Initialize Oddish."""
        super().__init__("Oddish", "Grass/Poison")

    def attack(self) -> str:
        """Perform Oddish's attack."""
        return "Oddish uses Absorb!"

    def heal(self, target: str | None = None) -> str:
        """Heal Oddish."""
        return "Oddish heals itself for a small amount"


class Vileplume(Creature, HealCapability):
    """Concrete healing creature (Evolved form)."""

    def __init__(self) -> None:
        """Initialize Vileplume."""
        super().__init__("Vileplume", "Grass/Poison")

    def attack(self) -> str:
        """Perform Vileplume's attack."""
        return "Vileplume uses Petal Dance!"

    def heal(self, target: str | None = None) -> str:
        """Heal Vileplume and allies."""
        return "Vileplume heals itself and others for a large amount"


class Zorua(Creature, TransformCapability):
    """Concrete transforming creature (Base form)."""

    def __init__(self) -> None:
        """Initialize Zorua."""
        super().__init__("Zorua", "Dark")
        self.is_transformed: bool = False

    def attack(self) -> str:
        """Perform Zorua's attack based on its form."""
        if self.is_transformed:
            return "Zorua performs a boosted illusion strike!"
        return "Zorua attacks normally."

    def transform(self) -> str:
        """Transform Zorua into its enhanced form (illusion)."""
        self.is_transformed = True
        return "Zorua creates an illusion and changes its form!"

    def revert(self) -> str:
        """Revert Zorua to its normal form."""
        self.is_transformed = False
        return "Zorua's illusion fades."


class Zoroark(Creature, TransformCapability):
    """Concrete transforming creature (Evolved form)."""

    def __init__(self) -> None:
        """Initialize Zoroark."""
        super().__init__("Zoroark", "Dark")
        self.is_transformed: bool = False

    def attack(self) -> str:
        """Perform Zoroark's attack based on its form."""
        if self.is_transformed:
            return "Zoroark unleashes a devastating illusion strike!"
        return "Zoroark attacks normally."

    def transform(self) -> str:
        """Transform Zoroark into its battle illusion form."""
        self.is_transformed = True
        return "Zoroark amplifies its illusion into a fearsome guise!"

    def revert(self) -> str:
        """Revert Zoroark to its stable form."""
        self.is_transformed = False
        return "Zoroark's illusion dissipates."
