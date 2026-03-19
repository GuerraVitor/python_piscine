import sys

def main():
    print("=== Player Score Analytics ===")

    args = sys.argv[1:]
    scores = []

    for arg in args:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Error: '{arg} is not a valid score (skipped)")

    if not args:
        print("No scores provides. Usage python3 ft_score_analytics.py "
        "<score1> <score2> ...")
    else:
        total_players = len(scores)
        total_score = sum(scores)
        average = total_score / total_players
        high = max(scores)
        low = min(scores)
        score_range = high - low

        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average}")
        print(f"High score: {high}")
        print(f"Low score: {low}")
        print(f"Score range: {score_range}\n")


if __name__ == "__main__":
    main()
