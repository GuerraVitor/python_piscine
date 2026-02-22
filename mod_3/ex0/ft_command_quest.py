"""Handle command-line arguments using sys.argv."""
import sys


def main():
    """Parse and display command-line arguments."""
    print("=== Command Quest ===")

    program_name = sys.argv[0]
    user_args = sys.argv[1:]
    if not user_args:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {len(user_args)}")

        for i, arg in enumerate(user_args, start=1):
            print(f"Argument {i}: {arg}")

        print(f"Total Arguments: {len(sys.argv)}\n")


if __name__ == "__main__":
    main()
