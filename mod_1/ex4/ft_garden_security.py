"""Protect plant data with validation before mutation."""


class Plant:
    """Keep plant attributes and simple mutations."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Seed name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        """Increase height."""
        self.height += cm

    def age_up(self, days: int) -> None:
        """Increase age."""
        self.age += days

    def get_info(self) -> str:
        """Return a status summary."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


class SecurePlant(Plant):
    """Wrap a plant with validation helpers."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Prevent negatives on creation."""
        sanitized_height = max(0, height)
        sanitized_age = max(0, age)
        super().__init__(name, sanitized_height, sanitized_age)
        self._height = self.height
        self._age = self.age
        print(f"Plant created: {self.name}")

    def set_height(self, height: int) -> None:
        """Assign height if non-negative."""
        if height < 0:
            print(
                f"Invalid operation attempted: height {height}cm "
                "[REJECTED]"
            )
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Assign age if non-negative."""
        if age < 0:
            print(
                f"Invalid operation attempted: age {age} days "
                "[REJECTED]"
            )
            print("Security: Negative age rejected")
            return
        self._age = age
        print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """Return the secured height."""
        return self._height

    def get_age(self) -> int:
        """Return the secured age."""
        return self._age

    def display_info(self) -> None:
        """Print the current secure plant status."""
        print(
            f"\nCurrent plant: {self.name} ({self._height}cm, "
            f"{self._age} days)"
        )


def main() -> None:
    """Drive the security scenario."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    plant.display_info()


if __name__ == "__main__":
    main()
