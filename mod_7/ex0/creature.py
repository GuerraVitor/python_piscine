"""Module defining various creature classes for a card game."""
from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract class representing a generic creature card."""

    def __init__(self, name: str, creature_type: str) -> None:
        """Initialize a creature with a name and type."""
        self.name: str = name
        self.creature_type: str = creature_type

    def describe(self) -> str:
        """Return a string describing the creature and its type."""
        return f"{self.name} is a {self.creature_type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        """Abstract method to return the creature's attack message."""
        pass


class Flameling(Creature):
    """A Fire-type creature card."""

    def __init__(self) -> None:
        """Initialize a creature of Flameling."""
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        """Return the creature's attack message."""
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    """A Fire/Flying-type creature card."""

    def __init__(self) -> None:
        """Initialize a creature of Pyrodon."""
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        """Abstract method to return the creature's attack message."""
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    """A Water-type creature card."""

    def __init__(self) -> None:
        """Initialize a creature of Aquabub."""
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        """Abstract method to return the creature's attack message."""
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    """A Water-type creature card."""

    def __init__(self) -> None:
        """Initialize a creature of Torragon."""
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        """Abstract method to return the creature's attack message."""
        return "Torragon uses Hydro Pump!"
