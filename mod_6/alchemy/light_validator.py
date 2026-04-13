"""Module for validating light magic ingredients."""


def validate_ingredients(ingredients: str) -> str:
    """Validate light ingredients."""
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    if any(i.lower() in ingredients.lower() for i in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
