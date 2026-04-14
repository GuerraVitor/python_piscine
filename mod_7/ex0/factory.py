"""Module defining factory methods for families."""
from abc import ABC, abstractmethod
from .creature import (
    Creature, Charmander, Charizard,
    Squirtle, Blastoise, Bulbasaur, Venusaur
)


class CreatureFactory(ABC):
    """Abstract factort interface for creating creatures. families."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base form of the family."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved form of the family."""
        pass


class FireFactory(CreatureFactory):
    """Factory for the fire family."""

    def create_base(self) -> Creature:
        """Create Charmander."""
        return Charmander()

    def create_evolved(self) -> Creature:
        """Return Charizard."""
        return Charizard()


class WaterFactory(CreatureFactory):
    """Factory for the water family."""

    def create_base(self) -> Creature:
        """Create Squirtle."""
        return Squirtle()

    def create_evolved(self) -> Creature:
        """Return Blastoise."""
        return Blastoise()


class GrassFactory(CreatureFactory):
    """Factory for the grass family."""

    def create_base(self) -> Creature:
        """Create Bulbasaur."""
        return Bulbasaur()

    def create_evolved(self) -> Creature:
        """Return Venusaur."""
        return Venusaur()
