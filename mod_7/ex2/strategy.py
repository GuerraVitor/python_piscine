"""Strategy abstractions and implementations for creature battles."""
from abc import ABC, abstractmethod
from typing import cast

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy is used with an incompatible creature."""


class BattleStrategy(ABC):
    """Abstract strategy for deciding how a creature acts in battle."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return whether this strategy can be used by the creature."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        """Return ordered action messages for this creature in battle."""
        pass


class NormalStrategy(BattleStrategy):
    """Default strategy: perform a single regular attack."""

    def is_valid(self, creature: Creature) -> bool:
        """Allow this strategy for any creature."""
        return True

    def act(self, creature: Creature) -> list[str]:
        """Execute normal battle behavior."""
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    """Transform-first strategy for transform-capable creatures."""

    def is_valid(self, creature: Creature) -> bool:
        """Aggressive strategy requires transform capability."""
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        """Transform, attack, then revert."""
        if not self.is_valid(creature):
            message = (
                "Invalid Creature "
                f"'{creature.name}' for this aggressive strategy"
            )
            raise InvalidStrategyError(
                message
            )

        transform_creature = cast(TransformCapability, creature)
        return [
            transform_creature.transform(),
            creature.attack(),
            transform_creature.revert(),
        ]


class DefensiveStrategy(BattleStrategy):
    """Heal-after-attack strategy for healing creatures."""

    def is_valid(self, creature: Creature) -> bool:
        """Defensive strategy requires heal capability."""
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        """Attack first, then heal."""
        if not self.is_valid(creature):
            message = (
                "Invalid Creature "
                f"'{creature.name}' for this defensive strategy"
            )
            raise InvalidStrategyError(
                message
            )

        heal_creature = cast(HealCapability, creature)
        return [creature.attack(), heal_creature.heal()]
