"""Protect plant data with validation before mutation."""


class SecurePlant:
    """Represent a plant with validated state."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Store the plant's basic data with validation."""
        self.name = name
        # Initialize private variables with sanitized values
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
        """Increase height safely."""
        self.set_height(self.get_height() + cm)

    def age_up(self, days: int) -> None:
        """Increase age safely."""
        self.set_age(self.get_age() + days)

    def get_info(self) -> str:
        """Return the plant summary."""
        return f"{self.name}: {self._height}cm, {self._age} days old"


def main() -> None:
    """Drive the security scenario."""
    print("=== Garden Security System ===")
    # Create a standard Plant (now secure by default)
    plant = SecurePlant("Rose", 25, 30)

    print(f"Created: {plant.get_info()}")

    print("\nAttempting to set negative height...")
    plant.set_height(-5)

    print("\nAttempting to set valid height...")
    plant.set_height(35)
    print(f"Updated: {plant.get_info()}")


if __name__ == "__main__":
    main()
