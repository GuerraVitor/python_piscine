"""Describe specialized garden plants and their behaviors."""


class Plant:
    """Track name, height, and age for any plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Store the shared plant data."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return a short descriptor."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


class Flower(Plant):
    """Flower type that can bloom."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
    ) -> None:
        """Register flower-specific data."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Announce that the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Tree type with trunk details."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        diameter: int,
    ) -> None:
        """Register tree-specific data."""
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    def produce_shade(self) -> None:
        """Announce how much shade the tree makes."""
        shade_area = self.trunk_diameter * 1.6
        print(
            f"{self.name} provides {shade_area:.0f} "
            "square meters of shade"
        )


class Vegetable(Plant):
    """Vegetable type with harvest info."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        """Register vegetable-specific data."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display_nutrition(self) -> None:
        """Announce the vegetable's nutrition."""
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    """Show specialized plant data."""
    print("=== Garden Plant Types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Lily", 35, 20, "pink"),
    ]
    for flower in flowers:
        print(
            f"{flower.name} (Flower): {flower.get_info()}, "
            f"{flower.color} color"
        )
        flower.bloom()

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Maple", 320, 900, 35),
    ]
    for tree in trees:
        print(
            f"{tree.name} (Tree): {tree.get_info()}, "
            f"{tree.trunk_diameter}cm diameter"
        )
        tree.produce_shade()

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 40, 65, "spring", "beta carotene"),
    ]
    for vegetable in vegetables:
        print(
            f"{vegetable.name} (Vegetable): {vegetable.get_info()}, "
            f"{vegetable.harvest_season} harvest"
        )
        vegetable.display_nutrition()


if __name__ == "__main__":
    main()
