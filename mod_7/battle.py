"""Module for testing Pokémon creature factories and simulating battles."""
from ex0 import CreatureFactory, FireFactory, WaterFactory, GrassFactory


def test_factory(factory: CreatureFactory) -> None:
    """Test factory creation and creature actions."""
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    """Simulate battle between base forms."""
    print("Testing battle")
    c1 = f1.create_base()
    c2 = f2.create_base()

    print(f"{c1.describe()}\nvs.\n{c2.describe()}\nfight!")
    print(c1.attack())
    print(c2.attack())


def main() -> None:
    """Entry point for the Pokémon battle simulation."""
    try:
        factories = [FireFactory(), WaterFactory(), GrassFactory()]

        for factory in factories:
            test_factory(factory)

        test_battle(factories[0], factories[2])
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
