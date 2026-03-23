import sys

def main():
    print("=== Inventory System Analysis ===\n")
    inventory = {}

    for arg in sys.argv[1:]:

        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - ivalid parameter '{arg}'")
            continue

        item = parts[0]
        qnt_str = parts[1]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            qty = int(qnt_str)
        except Exception as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        inventory.update({item: qty})

    if len(inventory) == 0:
        return

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory)}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for item in inventory:
        print(f"Item {item} represents {inventory[item]/total*100:.1f}%")

    for item in inventory:
        value = 0
        if inventory[item] > value:
            value = inventory[item]
            abundant = item
    print(f"Item most abundant: {abundant} with quantity {qty}")

if __name__ == "__main__":
    main()
