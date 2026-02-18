# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vguerra- <vguerra-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 18:02:01 by vguerra-          #+#    #+#              #
#    Updated: 2026/02/18 18:07:51 by vguerra-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    """
    Plant class with growth behaviors.
    """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm):
        """Increase plants height"""
        self.height += cm

    def age_up(self, days):
        """Increase plants age"""
        self.age += days

    def get_info(self):
        """"Returns plant current status."""
        return f"{self.name}: {self.height}cm, {self.age}days old"

def main():
    """Simulates one week of growth"""
    rose = Plant("Rose", 25, 30)
    start_height = rose.height

    print("=== Day 1 ===")
    print(rose.get_info())

    rose.grow(6)
    rose.age_up(6)

    print("\n=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - start_height}cm")

if __name__ == "__main__":
    main()
