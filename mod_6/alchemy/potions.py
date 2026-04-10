"""Module for brewing magical potions."""

import elements
from .elements import create_air, create_earth


def healing_potion() -> str:
    """Brew a healing potion."""
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"


def strength_potion() -> str:
    """Brew a strength potion."""
    return f"Strength potion brewed with '{elements.create_fire()}' and '{elements.create_water()}'"
