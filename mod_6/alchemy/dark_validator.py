"""Module for validating dark magic ingredients."""

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validate dark ingredients."""
    allowed = dark_spell_allowed_ingredients()
    if any(i.lower() in ingredients.lower() for i in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
