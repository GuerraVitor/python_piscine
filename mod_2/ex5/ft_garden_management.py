"""Combine error handling techniques into a robust garden manager."""


class GardenError(Exception):
    """Base class for all garden-related errors."""

    pass


class PlantError(GardenError):
    """Exception raised for plant health issues."""

    pass


class WaterError(GardenError):
    """Exception raised for watering supply issues."""

    pass


class GardenManager:
    """Manage garden operations with robust error handling."""

    def __init__(self):
        """Initialize an empty garden."""
        self.plants = []

    def add_plant(self, name):
        """Add a plant to the garden, validating the name."""
        if not name:
            raise ValueError("Plant name cannot be empty!")
        self.plants.append(name)
        print(f"Added {name} successfully")

    def water_plants(self):
        """Simulate watering with guaranteed cleanup."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name, water_level, sun_hours):
        """Check plant metrics and raise custom errors if invalid."""
        if water_level > 10:
            raise PlantError(f"Water level {water_level} is too high (max 10)")
        if sun_hours < 2:
            raise PlantError(f"Sunlight hours {sun_hours} is too low (min 2)")

        print(f"{name}: healthy (water: {water_level}, sun: {sun_hours})")

    def verify_tank(self):
        """Simulate a tank check that fails."""
        raise WaterError("Not enough water in tank")


def main():
    """Run the garden management system demo."""
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("\nAdding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
    except ValueError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("")
    except ValueError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
    except PlantError as e:
        print(f"Error checking tomato: {e}")

    try:
        manager.check_plant_health("lettuce", 15, 8)
    except PlantError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        manager.verify_tank()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
