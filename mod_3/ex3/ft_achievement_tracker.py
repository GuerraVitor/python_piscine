"""Track and analyze player achievements using sets."""


def main():
    """Demonstrate set operations for achievement tracking."""
    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievements Analytics ===")

    all_achievements = alice | bob | charlie
    print(f"All unique achievements: {(all_achievements)}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_all = alice & bob & charlie
    print(f"\nCommon to all players: {common_all}")

    rare_achievements = set()
    for achievement in all_achievements:
        count = 0
        if achievement in alice:
            count += 1
        if achievement in bob:
            count += 1
        if achievement in charlie:
            count += 1

        if count == 1:
            rare_achievements.add(achievement)

    print(f"Rare achievements (1 player): {sorted(rare_achievements)}")

    print(f"\nAlice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    main()
