"""Alchemy package for creating elemental objects."""

__version__ = "1.0.0"
__author__ = "Vitor Guerra"

from .elements import create_air
from .potions import strength_potion, healing_potion as heal
from . import transmutation

__all__ = ["create_air", "strength_potion", "heal", "transmutation"]
