"""Module to test the dark spell recording, expecting an explosion."""

print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION", flush=True)

# This will trigger a circular import exception
from alchemy.grimoire.dark_spellbook import dark_spell_record
