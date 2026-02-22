"""Validate plant health metrics using explicit error raising."""


def check_plant_health(plant_name, water_level, sun_hours):
    """Validade plant data and raise errors for invalid values."""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sun_hours < 2:
        raise ValueError(f"Sunlight hours {sun_hours} is too low (min 2)")
    if sun_hours > 12:
        raise ValueError(f"Sunlight hours {sun_hours} is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Run tests to demonstrate error raising and handling."""
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        msg = check_plant_health("tomato", 5, 6)
        print(msg)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("lettuce", 15, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("sunflower", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising test completed!")


if __name__ == "__main__":
    test_plant_checks()
