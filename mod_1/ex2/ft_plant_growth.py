# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vguerra- <vguerra-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 18:02:01 by vguerra-          #+#    #+#              #
#    Updated: 2026/02/20 13:40:37 by vguerra-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    """Represent a garden plant with mutable state."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Store the plant's starting values."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        """Increase the plant height."""
        self.height += cm

    def age_up(self, days: int) -> None:
        """Advance the plant age."""
        self.age += days

    def get_info(self) -> str:
        """Return a formatted status line."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    """Simulate a week of growth for multiple plants."""
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    growth_plan = [
        (6, 6),
        (12, 6),
        (4, 6),
    ]

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    for plant, (growth_cm, days) in zip(plants, growth_plan):
        plant.grow(growth_cm)
        plant.age_up(days)

    print("\n=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())

    print("\nGrowth this week:")
    for plant, (growth_cm, _) in zip(plants, growth_plan):
        print(f"{plant.name}: +{growth_cm}cm")


if __name__ == "__main__":
    main()
