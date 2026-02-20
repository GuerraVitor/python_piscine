# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vguerra- <vguerra-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 18:14:47 by vguerra-          #+#    #+#              #
#    Updated: 2026/02/20 10:38:44 by vguerra-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    """Base class for plants"""

    def __init__(self, name:str, height: int, age: int):
        """Initialize and display creation confirmation"""
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

def main() -> None:
    """creates different plants efficiently"""
    print("=== Plant Factory Output ===")

    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    plants = []
    for data in plant_data:
        plants.append(Plant(*data))

    print(f"\nTotal plants created: {len(plants)}")

if __name__ == "__main__":
    main()
