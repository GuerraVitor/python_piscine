"""Module for light magic spells."""

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    """Return allowed light ingredients."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a light spell."""
    validation = validate_ingredients(ingredients)
    status = "rejected" if "INVALID" in validation else "recorded"
    return f"Spell {status}: {spell_name} ({validation})"
