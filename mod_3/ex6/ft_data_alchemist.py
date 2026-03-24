"""Perform data alchemy on game data."""
import random


def main() -> None:
    """Perform various data manipulations on a list of players."""
    print("=== Game Data Alchemist ===\n")
    all_players: list[str] = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                              'Gregory', 'john', 'kevin', 'Liam']

    all_capitalized: list[str] = [name.capitalize() for name in all_players]

    only_capitalized: list[str] = [name for name in all_players if
                                   name[0] >= 'A' and name[0] <= 'Z']

    score_dict: dict[str, int] = {name: random.randint(0, 1000)
                                  for name in all_capitalized}

    total_score: int = sum(score_dict.values())
    average_score: float = total_score / len(score_dict)

    high_scores: dict[str, int] = {name: score for name, score in
                                   score_dict.items() if score > average_score}

    print(f"Initial list of players: {all_players}")
    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {only_capitalized}")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {round(average_score, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
