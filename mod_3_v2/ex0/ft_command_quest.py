"""Handle command-line arguments using sys.argv."""
import sys

def main():
    """Parse and display command-line arguments."""
    print(f"=== Command Quest ===")

    prog_name = sys.argv[0]
    args_receives = sys.argv[1:]

    count_args = len(args_receives)
    if count_args == 0:
        print(f"No arguments provided!")

    print(f"Program name: {prog_name}")

    if count_args > 0:
        print(f"Arguments received: {count_args}")
        for i, arg in enumerate(args_receives, start=1):
            print(f"Argument {i}: {arg}")

    print(f"Total arguments: {count_args+1}\n")

if __name__ == "__main__":
    main()
