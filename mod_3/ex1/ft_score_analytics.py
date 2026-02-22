"""Calculates and display statistics from command-line scores."""
import sys


def main():
    """Process scores and print analytics."""
    print("=== Player Score Analytics ===")

    raw_args = sys.argv[1:]
    scores = []

    for arg in raw_args:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Error: '{arg} is not a valid score (skipped)")

    if not scores:
        print("No scores provided. usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.1f}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}\n")


if __name__ == "__main__":
    main()
