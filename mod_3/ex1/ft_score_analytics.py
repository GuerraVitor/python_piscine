"""analyzing data received via command line."""
import sys


def main() -> None:
    """Parse and manipule data received via the command line."""
    print("=== Player Score Analytics ===")

    args: list[str] = sys.argv[1:]
    scores: list[int] = []

    for arg in args:
        try:
            score: int = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Error: '{arg} is not a valid score (skipped)")

    if not args:
        print("No scores provides. Usage python3 ft_score_analytics.py"
              "<score1> <score2> ...")

    else:
        total_players: int = len(scores)
        total_score: int = sum(scores)
        average: float = total_score / total_players
        high: int = max(scores)
        low: int = min(scores)
        score_range: int = high - low

        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average}")
        print(f"High score: {high}")
        print(f"Low score: {low}")
        print(f"Score range: {score_range}\n")


if __name__ == "__main__":
    main()
