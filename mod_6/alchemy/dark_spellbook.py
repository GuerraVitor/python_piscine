"""Module for dark magic spells."""

from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return allowed dark ingredients."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a dark spell."""
    validation = validate_ingredients(ingredients)
    status = "rejected" if "INVALID" in validation else "recorded"
    return f"Spell {status}: {spell_name} ({validation})"
