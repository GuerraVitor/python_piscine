# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vguerra- <vguerra-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/20 11:12:18 by vguerra-          #+#    #+#              #
#    Updated: 2026/02/20 12:08:18 by vguerra-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    """Base class for all garden plants"""

    def __init__(self, name:str, height: int, age: int):
        """Initialize secure plant with validations"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

class Flower(Plant):
    """flower type with blooming ability"""

    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Action specific to flowers"""
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
    """"Tree type with trunk diameter and shade ability"""

    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.diameter: int = diameter

    def produce_shade(self) -> None:
        """Action specify to trees"""
        print(f"{self.name} provides 78 squares meters of shade")

class Vegetable(Plant):
    """Vegetable type with nutrition and harvest info"""

    def __init__(self, name: str, height: int, age: int, season: str, vit: str):
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: str = vit

    def display_nutrition(self) -> None:
        """Display begetable nutrition info"""
        print(f"{self.name} is rich in {self.nutritional_value}")

