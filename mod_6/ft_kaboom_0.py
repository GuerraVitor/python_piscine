"""Module for testing light magic spells."""

import alchemy.grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print(
    f"Testing record light spell: {alchemy.grimoire.light_spell_record('Fantasy', 'Earth, wind and fire')}"
)
