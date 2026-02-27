"""Build a simple analytics dashboard using Python comprehensions."""


def main():
    """Demonstrate list, dict and set comprehensions with game data."""
    print("=== Game Analytics Dashboard ===")

    players = [
        {
            "name": "alice", "score": 2300, "achievements": 5,
            "active": True, "region": "north"
        },
        {
            "name": "bob", "score": 1800, "achievements": 3,
            "active": True, "region": "east"
        },
        {
            "name": "charlie", "score": 2150, "achievements": 7,
            "active": False, "region": "central"
        },
        {
            "name": "diana", "score": 2050, "achievements": 4,
            "active": True, "region": "north"
        },
        {
            "name": "eve", "score": 1200, "achievements": 2,
            "active": False, "region": "west"
        }
    ]

    events = [
        {"player": "alice", "achievement": "first_kill"},
        {"player": "alice", "achievement": "level_10"},
        {"player": "bob", "achievement": "first_kill"},
        {"player": "charlie", "achievement": "boss_slayer"},
        {"player": "diana", "achievement": "level_10"},
        {"player": "eve", "achievement": "collector"},
        {"player": "charlie", "achievement": "speed_demon"}
    ]

    print("\n=== List Comprehension Examples ===")
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    doubled_scores = [p["score"] * 2 for p in players]
    active_players = [p["name"] for p in players if p["active"]]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in players}
    player_achievements = {p["name"]: p["achievements"] for p in players}
    categories = {
        p["name"]: (
            "high" if p["score"] >= 2000
            else "medium" if p["score"] >= 1500
            else "low"
        )
        for p in players
    }
    score_categories = {
        category: len([name for name in categories if categories[name] == category])
        for category in ["high", "medium", "low"]
    }

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {player_achievements}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {event["player"] for event in events}
    unique_achievements = {event["achievement"] for event in events}
    active_regions = {p["region"] for p in players if p["active"]}

    print(f"Unique players: {sorted(unique_players)}")
    print(f"Unique achievements: {sorted(unique_achievements)}")
    print(f"Active regions: {sorted(active_regions)}")

    print("\n=== Combined Analysis ===")
    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum([p["score"] for p in players]) / total_players
    ranking = sorted(
        [(p["score"], p["name"], p["achievements"]) for p in players],
        reverse=True
    )
    top_score, top_player, top_achievements = ranking[0]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {top_player} "
        f"({top_score} points, {top_achievements} achievements)"
    )


if __name__ == "__main__":
    main()
