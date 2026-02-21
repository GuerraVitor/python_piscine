"""Describe specialized garden plants and their behaviors."""


class Plant:
    """Represent a plant with validated state."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Store the plant's basic data with validation."""
        self.name = name
        self._height = max(0, height)
        self._age = max(0, age)

    def get_height(self) -> int:
        """Return the secured height."""
        return self._height

    def set_height(self, height: int) -> None:
        """Assign height if non-negative."""
        if height < 0:
            print(f"Error: height {height} is invalid (must be non-negative)")
            return
        self._height = height

    def get_age(self) -> int:
        """Return the secured age."""
        return self._age

    def set_age(self, age: int) -> None:
        """Assign age if non-negative."""
        if age < 0:
            print(f"Error: age {age} is invalid (must be non-negative)")
            return
        self._age = age

    def grow(self, cm: int) -> None:
        """Grow by centimeters."""
        self.set_height(self.get_height() + cm)

    def age_up(self, days: int) -> None:
        """Age by days."""
        self.set_age(self.get_age() + days)

    def get_info(self) -> str:
        """Return the plant summary."""
        return f"{self.name}: {self._height}cm, {self._age} days old"


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
        print(f"{self.name} is blooming beautifully!\n")


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
            "square meters of shade\n"
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
        print(f"{self.name} is rich in {self.nutritional_value}\n")


def main() -> None:
    """Show specialized plant data."""
    print("=== Garden Plant Types ===\n")

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
