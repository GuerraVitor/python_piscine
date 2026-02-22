"""Define and demonstrate custom exception classes."""


class GardenError(Exception):
    """Base class for all garden-related errors."""

    pass


class PlantError(GardenError):
    """Exception raised for plant health issues."""

    pass


class WaterError(GardenError):
    """Execption raised for watering supply issues."""

    pass


def test_custom_errors():
    """Demonstrate raising and catching custom exceptions."""
    print("=== Custom Garden Erros Demo ===")

    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden erros...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
