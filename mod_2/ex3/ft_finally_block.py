"""Demonstrate the use of the finally block for resource cleanup."""


def water_plants(plant_list):
    """Simulate watering plants with guaranteed cleanup."""
    try:
        print("Opening watering system")
        for plant in plant_list:
            if not isinstance(plant, str):
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test the watering function with valid and invalid lists."""
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    bad_plants = ["tomato", None, "carrots"]
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
