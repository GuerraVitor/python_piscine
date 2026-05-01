"""Module defining factories for specialized creatures."""
from ex0.factory import CreatureFactory
from ex0.creature import Creature
from .creature import Oddish, Vileplume, Zorua, Zoroark


class HealingCreatureFactory(CreatureFactory):
    """Factory for creating creatures with healing capabilities."""

    def create_base(self) -> Creature:
        """Create the base healing creature."""
        return Oddish()

    def create_evolved(self) -> Creature:
        """Create the evolved healing creature."""
        return Vileplume()


class TransformCreatureFactory(CreatureFactory):
    """Factory for creating creatures with transform capabilities."""

    def create_base(self) -> Creature:
        """Create the base transforming creature."""
        return Zorua()

    def create_evolved(self) -> Creature:
        """Create the evolved transforming creature."""
        return Zoroark()
