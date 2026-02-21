"""Garden analytics combining plant families, stats, and manager helpers."""


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


class FloweringPlant(Plant):
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
        self.is_blooming = False

    def bloom(self) -> str:
        """Mark the plant as blooming and return a descriptor."""
        self.is_blooming = True
        return f"{self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Flowering plant that earns prize points."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        prize_points: int,
    ) -> None:
        """Store prize-specific data on top of the flower traits."""
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def award_points(self) -> str:
        """Summarize the prize contribution."""
        return f"Prize points: {self.prize_points}"

    def get_info(self) -> str:
        """Include bloom status and prize info in the summary."""
        base = super().get_info()
        bloom = self.bloom()
        prize = self.award_points()
        return f"{base}, {bloom}, {prize}"


class GardenManager:
    """Manage gardens, plants, and analytics flows."""

    gardens: list["GardenManager"] = []

    class GardenStats:
        """Collect counts and growth totals."""

        def __init__(self) -> None:
            """Initialize counters for the garden."""
            self.plants_added = 0
            self.total_growth = 0
            self.type_counts = {
                "regular": 0,
                "flowering": 0,
                "prize": 0,
            }

        def register(self, plant: Plant) -> None:
            """Update the stats when a plant joins."""
            self.plants_added += 1
            if isinstance(plant, PrizeFlower):
                self.type_counts["prize"] += 1
            elif isinstance(plant, FloweringPlant):
                self.type_counts["flowering"] += 1
            else:
                self.type_counts["regular"] += 1

        def register_growth(self, amount: int) -> None:
            """Track applied growth."""
            self.total_growth += amount

        def summary(self) -> str:
            """Return a short summary of the garden's stats."""
            counts = self.type_counts
            return (
                f"Plants added: {self.plants_added}, "
                f"Total growth: {self.total_growth}cm\n"
                f"Plant types: {counts['regular']} regular, "
                f"{counts['flowering']} flowering, "
                f"{counts['prize']} prize flowers"
            )

    def __init__(self, owner: str) -> None:
        """Prepare the garden manager and register it."""
        self.owner = owner
        self.plants: list[Plant] = []
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens.append(self)

    def add_plant(self, plant: Plant) -> None:
        """Add a plant if its height is valid."""
        if not GardenManager.validate_height(plant.get_height()):
            print(f"Cannot add {plant.name}: invalid height")
            return
        self.plants.append(plant)
        self.stats.register(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """Apply a single growth cycle to every plant."""
        if not self.plants:
            return
        print(f"{self.owner} is helping all plants grow...")
        growth = 0
        for plant in self.plants:
            plant.grow(1)
            plant.age_up(1)
            growth += 1
            print(f"{plant.name} grew 1cm")
        self.stats.register_growth(growth)

    def report(self) -> None:
        """Print the garden report using the nested stats helper."""
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.get_info()}")
            elif isinstance(plant, FloweringPlant):
                bloom = plant.bloom()
                print(f"- {plant.name}: {plant.get_height()}cm, {bloom}")
            else:
                print(f"- {plant.name}: {plant.get_height()}cm")
        print(self.stats.summary())

    @classmethod
    def create_garden_network(cls, names: list[str]) -> list["GardenManager"]:
        """Build multiple managers at once."""
        return [cls(name) for name in names]

    @classmethod
    def garden_scores(cls) -> dict[str, int]:
        """Score each garden based on height, growth, and headcount."""
        scores: dict[str, int] = {}
        for garden in cls.gardens:
            height_total = sum(plant.get_height() for plant in garden.plants)
            scores[garden.owner] = (
                height_total + garden.stats.plants_added * 7
                + garden.stats.total_growth * 5
            )
        return scores

    @staticmethod
    def validate_height(value: int) -> bool:
        """Validate that a height value is non-negative."""
        return value >= 0


def main() -> None:
    """Display the garden analytics platform."""
    print("\n=== Garden Management System Demo ===")
    alice, bob = GardenManager.create_garden_network(["Alice", "Bob"])

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    bob.add_plant(Plant("Sprout", 10, 5))

    alice.grow_all()
    bob.grow_all()

    alice.report()
    bob.report()

    print(f"Height validation test: {GardenManager.validate_height(30)}")
    scores = GardenManager.garden_scores()
    pairs = ", ".join(f"{owner}: {score}" for owner, score in scores.items())
    print(f"\nGarden scores - {pairs}")
    print(f"Total gardens managed: {len(GardenManager.gardens)}\n")


if __name__ == "__main__":
    main()
