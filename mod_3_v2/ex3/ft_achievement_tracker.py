import random

def gen_player_achiev(achievements):

    n = random.randint(5,8)
    return set(random.sample(list(achievements), n))

def main():


    achievements = {
        "First Steps", "Master Explorer", "Boss Slayer",
        "Collector Supreme", "Untouchable", "Strategist",
        "Speed Runner", "Treasure Hunter", "Sharp Mind",
        "World Savior", "Survivor", "Unstoppable",
        "Hidden Path Finder"
    }

    print("=== Achievmenent Tracker System ===")

    alice = set(gen_player_achiev(achievements))
    bob = set(gen_player_achiev(achievements))
    charlie = set(gen_player_achiev(achievements))
    dylan = set(gen_player_achiev(achievements))

    print(f"\nPlayer Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print(f"\nAll distinct achievements: {alice.union(bob, charlie, dylan) }")
    print(f"\nCommon achievements: {alice.intersection(bob, charlie, dylan) }")

    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}")

    print(f"\nAlice is missing: {achievements.difference(alice)}")
    print(f"Bob is missing: {achievements.difference(bob)}")
    print(f"Charlie is missing: {achievements.difference(charlie)}")
    print(f"Dylan is missing: {achievements.difference(dylan)}")

if __name__ == "__main__":
    main()
