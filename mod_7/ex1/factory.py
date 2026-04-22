"""Module defining factories for specialized creatures."""
from ex0.factory import CreatureFactory
from ex0.creature import Creature
from .creature import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    """Factory for creating creatures with healing capabilities."""

    def create_base(self) -> Creature:
        """Create the base healing creature."""
        return Sproutling()

    def create_evolved(self) -> Creature:
        """Create the evolved healing creature."""
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """Factory for creating creatures with transform capabilities."""

    def create_base(self) -> Creature:
        """Create the base transforming creature."""
        return Shiftling()

    def create_evolved(self) -> Creature:
        """Create the evolved transforming creature."""
        return Morphagon()
