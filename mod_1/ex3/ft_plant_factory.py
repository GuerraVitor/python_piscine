# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vguerra- <vguerra-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 18:14:47 by vguerra-          #+#    #+#              #
#    Updated: 2026/02/20 13:40:37 by vguerra-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    """Represent a plant with adjustable state."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Store the plant's basic data."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        """Grow by centimeters."""
        self.height += cm

    def age_up(self, days: int) -> None:
        """Age by days."""
        self.age += days

    def get_info(self) -> str:
        """Return the plant summary."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def create_plant(record: tuple[str, int, int]) -> Plant:
    """Create and announce a new plant from data."""
    plant = Plant(*record)
    print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    return plant


def main() -> None:
    """Run the factory output for a batch of plants."""
    print("=== Plant Factory Output ===")
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = [create_plant(data) for data in plant_data]
    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()
