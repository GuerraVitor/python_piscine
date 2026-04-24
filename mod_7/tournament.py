"""Tournament script for strategy-based creature battles."""
from ex0 import CreatureFactory, FireFactory, WaterFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


Opponent = tuple[CreatureFactory, BattleStrategy]


def _strategy_name(strategy: BattleStrategy) -> str:
    """Return a short readable name for a strategy."""
    if isinstance(strategy, NormalStrategy):
        return "Normal"
    if isinstance(strategy, AggressiveStrategy):
        return "Aggressive"
    if isinstance(strategy, DefensiveStrategy):
        return "Defensive"
    return strategy.__class__.__name__


def _factory_label(factory: CreatureFactory) -> str:
    """Return a readable family label for tournament printing."""
    if isinstance(factory, HealingCreatureFactory):
        return "Healing"
    if isinstance(factory, TransformCreatureFactory):
        return "Transform"
    return factory.create_base().name


def describe_opponents(opponents: list[Opponent]) -> str:
    """Build a compact textual representation of tournament opponents."""
    parts = [
        f"({_factory_label(factory)}+{_strategy_name(strategy)})"
        for factory, strategy in opponents
    ]
    return "[ " + ", ".join(parts) + " ]"


def run_tournament(opponents: list[Opponent]) -> None:
    """Run a round-robin tournament with strategy-aware actions."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_1, strategy_1 = opponents[i]
                factory_2, strategy_2 = opponents[j]
                creature_1 = factory_1.create_base()
                creature_2 = factory_2.create_base()

                print("* Battle *")
                print(creature_1.describe())
                print("vs.")
                print(creature_2.describe())
                print("now fight!")

                for action in strategy_1.act(creature_1):
                    print(action)
                for action in strategy_2.act(creature_2):
                    print(action)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    """Execute the requested tournament scenarios."""
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    tournament_0 = [
        (FireFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ]

    tournament_1 = [
        (FireFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ]

    tournament_2 = [
        (WaterFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ]

    print("Tournament 0 (basic)")
    print(describe_opponents(tournament_0))
    run_tournament(tournament_0)

    print("\nTournament 1 (error)")
    print(describe_opponents(tournament_1))
    run_tournament(tournament_1)

    print("\nTournament 2 (multiple)")
    print(describe_opponents(tournament_2))
    run_tournament(tournament_2)


if __name__ == "__main__":
    main()
