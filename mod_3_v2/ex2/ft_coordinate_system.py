import sys
import math

def calculate_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def get_player_pos():
    while True:
        coord_str = input("Enter new coordinates as float in format 'x,y,z': ")

        parts = coord_str.split(',')

        if len(parts) != 3:
            print("Invalid syntax: expected exactly 3 values.")
            continue

        parsed_parts = []

        for part in parts:
            try:
                parsed_parts.append(float(part))
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                break

        else:
            return tuple(parsed_parts)

def main():
    print("=== Game Coordinate System ===")
    points = get_player_pos()
    print(f"Got a fist tuple: {points}")

    x1, y1, z1 = points
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dist = calculate_distance((0,0,0), points)
    print(f"Distance to center: {dist:.4f}\n")

    print("Get a second set of coordinates")
    points2 = get_player_pos()
    dist = calculate_distance(points, points2)
    print(f"Distance between the 2 sets of coordinates: {dist:.4f}")

if __name__ == "__main__":
    main()
