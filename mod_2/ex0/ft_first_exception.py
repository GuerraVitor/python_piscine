"""Handle basic exceptions for temperature validation."""


def check_temperature(temp_str):
    """Validate temperature input."""
    try:
        temp = int(temp_str)

        if temp < 0:
            print(f"Error: {temp}ºC is too cold (min 0ºC)\n")
        elif temp > 40:
            print(f"Error: {temp}ºC is too hot (max 40ºC)\n")
        else:
            print(f"Temperature {temp}ºC is good!\n")
            return temp

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")

    return None


def test_temperature_input():
    """Run a suite of tests to demonstrate error handling."""
    print("=== Garden Temperature Checker ===\n")

    test_cases = ["25", "abc", "111", "-42"]

    for value in test_cases:
        print(f"Testing temperature: {value}")
        check_temperature(value)

    print("All tests completed - program didn't crash :)")


if __name__ == "__main__":
    test_temperature_input()
