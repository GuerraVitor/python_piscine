"""Welcome message for the garden introduction."""


def main() -> None:
    """Show the starting plant details."""
    name: str = "Rose"
    height: str = "25cm"
    age: str = "30 days"

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}")
    print(f"Age: {age}")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
