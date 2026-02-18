# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vguerra- <vguerra-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 18:02:04 by vguerra-          #+#    #+#              #
#    Updated: 2026/02/18 18:02:05 by vguerra-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    """represents a plant with a name, height, and age."""

    def __init__(self, name: str, height: int, age: int):
        "initializes the plants attributes"
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        """Display formatted plant information."""
        print(f"{self.name}: {self.height}cm, {self.age}days old")

def main() -> None:
    """Creates and displays gardens log."""
    print("=== Garden Plant Registry ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    for plant in plants:
        plant.display()

if __name__ == "__main__":
    main()
