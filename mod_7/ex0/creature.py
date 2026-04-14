"""Module defining creature families for a card game."""
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


class Charmander(Creature):
    """Concrete implementation of Charmander."""

    def __init__(self) -> None:
        """Initialize Charmander."""
        super().__init__("Charmander", "Fire")

    def attack(self) -> str:
        """Return Charmander's attack."""
        return "Charmander uses Ember!"


class Charizard(Creature):
    """Concrete implementation of Charizard."""

    def __init__(self) -> None:
        """Initialize Charizard."""
        super().__init__("Charizard", "Fire/Flying")

    def attack(self) -> str:
        """Return Charizard's attack."""
        return "Charizard uses Flamethrower!"


class Squirtle(Creature):
    """Concrete implementation of Squirtle."""

    def __init__(self) -> None:
        """Initialize Squirtle."""
        super().__init__("Squirtle", "Water")

    def attack(self) -> str:
        """Return Squirtle's attack."""
        return "Squirtle uses Water Gun!"


class Blastoise(Creature):
    """Concrete implementation of Blastoise."""

    def __init__(self) -> None:
        """Initialize Blastoise."""
        super().__init__("Blastoise", "Water")

    def attack(self) -> str:
        """Return Blastoise's attack."""
        return "Blastoise uses Hydro Pump!"


class Bulbasaur(Creature):
    """Concrete implementation of Bulbasaur."""

    def __init__(self) -> None:
        """Initialize Bulbasaur."""
        super().__init__("Bulbasaur", "Grass/Poison")

    def attack(self) -> str:
        """Return Bulbasaur's attack."""
        return "Bulbasaur uses Vine Whip!"


class Venusaur(Creature):
    """Concrete implementation of Venusaur."""

    def __init__(self) -> None:
        """Initialize Venusaur."""
        super().__init__("Venusaur", "Grass/Poison")

    def attack(self) -> str:
        """Return Venusaur's attack."""
        return "Venusaur uses Solar Beam!"
