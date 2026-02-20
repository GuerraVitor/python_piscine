# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vguerra- <vguerra-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/20 10:40:50 by vguerra-          #+#    #+#              #
#    Updated: 2026/02/20 11:10:34 by vguerra-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class SecurePlant:
    """A plant class with data validation"""

    def __init__(self, name: str, heihgt: int, age: int):
        """Initialize secure plant with validations"""
        self._name = name
        self._height = max(0, heihgt)
        self._age = max(0, age)
        print(f"Plant created: {self._name}")

    def set_height(self, height: int) -> None:
        """Update height if the value is non-negative"""
        if height < 0:
            print(f"Invalide operation attempted: heihgt {height}cm [REJECTED]")
            print("Security: negative heihght rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Update age if the value is non-negative"""
        if age < 0:
            print(f"Invalide operation attempted: age {age} days [REJECTED]")
            print("Security: negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """Return height"""
        return self._height

    def get_age(self) -> int:
        """Return age"""
        return self._age

    def display_info(self) -> None:
        """Show current plant status"""
        print(f"Current plant: {self._name} ({self._height}cm, {self._age} days)")

