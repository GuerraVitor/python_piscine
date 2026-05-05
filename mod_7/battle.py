"""Battle script for the Creature Factory exercise."""
from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    """Create and exercise both creatures from one factory."""
    print("Testing factory")
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print()


def test_battle(first_factory: FlameFactory,
                second_factory: AquaFactory) -> None:
    """Make the base creatures from two factories fight."""
    print("Testing battle")
    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()

    print(f"{first_creature.describe()}\nvs.\n{second_creature.describe()}")
    print("fight!")
    print(first_creature.attack())
    print(second_creature.attack())


def main() -> None:
    """Run the subject's sample scenario."""
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()

        test_factory(flame_factory)
        test_factory(aqua_factory)
        test_battle(flame_factory, aqua_factory)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
