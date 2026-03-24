"""Provide a simple inventory system analysis."""
import sys


def main() -> None:
    """Analyze inventory data from command-line arguments."""
    print("=== Inventory System Analysis ===\n")
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:

        parts: list[str] = arg.split(":")
        if len(parts) != 2:
            print(f"Error - ivalid parameter '{arg}'")
            continue

        item: str = parts[0]
        qnt_str: str = parts[1]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            qty: int = int(qnt_str)
        except Exception as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        inventory.update({item: qty})

    if len(inventory) == 0:
        return

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory)}")
    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for item in inventory:
        print(f"Item {item} represents {inventory[item]/total*100:.1f}%")

    value: int = 0
    abundant: str = ""
    for item in inventory:
        if inventory[item] > value:
            value = inventory[item]
            abundant = item
    print(f"Item most abundant: {abundant} with quantity {value}")

    value = 1000000
    for item in inventory:
        if inventory[item] < value:
            value = inventory[item]
            abundant = item
    print(f"Item least abundant: {abundant} with quantity {value}")

    inventory.update({'magic_item': 1})
    print(f"Update inventory: {inventory}")


if __name__ == "__main__":
    main()
