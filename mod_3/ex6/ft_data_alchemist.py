"""Perform data alchemy on game data."""
import random


def main():
    """Perform various data manipulations on a list of players."""
    print("=== Game Data Alchemist ===\n")
    all_players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
                   'john', 'kevin', 'Liam']

    all_capitalized = [name.capitalize() for name in all_players]

    only_capitalized = [name for name in all_players if
                        name[0] >= 'A' and name[0] <= 'Z']

    score_dict = {name: random.randint(0, 1000) for name in all_capitalized}

    total_score = sum([score_dict[name] for name in score_dict])
    average_score = total_score / len(score_dict)

    high_scores = {name: score_dict[name] for name in score_dict if
                   score_dict[name] > average_score}

    print(f"Initial list of players: {all_players}")
    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {only_capitalized}")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {round(average_score, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
