# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vguerra- <vguerra-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 18:02:04 by vguerra-          #+#    #+#              #
#    Updated: 2026/02/20 13:34:42 by vguerra-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    """Store a plant's name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with its basic values."""
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        """Show the plant's data in a tidy line."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """Build and display the plant registry."""
    print("=== Garden Plant Registry ===")

    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    for plant in plants:
        plant.display_info()


if __name__ == "__main__":
    main()
