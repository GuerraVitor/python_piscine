"""Manage 3D coordinates using tuples and math operations."""
import math


def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two 3D points."""
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def parse_coordinates(coord_str):
    """Parse a string 'x,y,z' into a tuple (x, y, z)."""
    print(f'\nParsing coordinates: "{coord_str}"')
    try:
        parts = coord_str.split(',')
        coords = tuple(map(int, parts))

        print(f"Parsed position: {coords}")
        return coords

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - type: {type(e).__name__}, Args: {e.args}")
        return None


def main():
    """Demonstrate 3D coordinate system features."""
    print("=== Game Coordinate System ===")

    spawn_point = (10, 20, 5)
    origin = (0, 0, 0)
    print(f"\nPosition created: {spawn_point}")

    dist = calculate_distance(origin, spawn_point)
    print(f"Distance between {origin} and {spawn_point}: {dist:.2f}")

    input_str = "3,4,0"
    player_pos = parse_coordinates(input_str)

    if player_pos:
        dist = calculate_distance(origin, player_pos)
        print(f"Distance Between {origin} and {player_pos}: {dist}")

    parse_coordinates("abc,bdc,cde")

    if player_pos:
        print("\nUnpacking demonstration:")
        x, y, z = player_pos
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
