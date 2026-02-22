"""Demonstrate handling of specific exception types."""


def garden_operations(action):
    """Simulate garden operation that might fail."""
    if action == "plant_count":
        return int("five")
    elif action == "water_distribution":
        water_litters = 100
        plants = 0
        return water_litters / plants
    elif action == "load_config":
        return open("config_garden_file.txt", "r")
    elif action == "check_inventory":
        inventory = {"seeds": 50}
        return inventory["shovels"]


def test_error_types():
    """Trigger and catch specific erros sequentially."""
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        garden_operations("plant_count")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("water_distribution")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("load_config")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("\nTesting KeyError...")
    try:
        garden_operations("check_inventory")
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("plant_count")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
