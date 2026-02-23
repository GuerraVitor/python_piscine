"""Manage player inventories using dictionaries."""


def display_inventory(player_name, inventory):
    """Print formatted inventory details and stats."""
    print(f"=== {player_name}'s Inventory ===")

    total_value = 0
    total_items = 0
    categories = {}

    for item_name, details, in inventory.items():
        qty = details['quantity']
        price = details['price']
        category = details['type']

        item_total = qty * price
        total_value += item_total
        total_items += qty

        categories[category] = categories.get(category, 0) + qty

        print(f"{item_name} ({category}, {details['rarity']}): "
              f"{qty}x @ {price} gold each = {item_total} gold")

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    cat_str = ", ".join([f"{k}({v})" for k, v in categories.items()])
    print(f"Categories: {cat_str}\n")

    return total_value, total_items


def main():
    """Demonstrate dictionary operations for inventory management."""
    print("=== Player Inventory System ===\n")

    alice_inv = {
        "sword": {
            "price": 500, "quantity": 1, "type": "weapon", "rarity": "rare"
        },
        "potion": {
            "price": 50, "quantity": 5, "type": "consumable",
            "rarity": "common"
        },
        "shield": {
            "price": 200, "quantity": 1, "type": "armor", "rarity": "uncommon"
        }
    }

    bob_inv = {
        "magic_ring": {
            "price": 1000, "quantity": 1, "type": "accessory",
            "rarity": "legendary"
        }
    }

    alice_val, alice_count = display_inventory("Alice", alice_inv)

    print("=== Transaction: Alice gives Bob 2 potions ===")

    item_name = "potion"
    amount = 2

    if item_name in alice_inv and alice_inv[item_name]['quantity'] >= amount:
        alice_inv[item_name]['quantity'] -= amount

        if item_name not in bob_inv:
            bob_inv[item_name] = alice_inv[item_name].copy()
            bob_inv[item_name]['quantity'] = 0

        bob_inv[item_name]['quantity'] += amount
        print("Transaction successful!\n")
    else:
        print("Transaction failed: Not enough items.\n")

    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice_inv['potion']['quantity']}")
    print(f"Bob potions: {bob_inv.get('potion', {}).get('quantity', 0)}")
    print()

    print("=== Inventory Analytics ===")
    alice_total = sum(i['price'] * i['quantity'] for i in alice_inv.values())
    bob_total = sum(i['price'] * i['quantity'] for i in bob_inv.values())

    if alice_total > bob_total:
        print(f"Most valuable player: Alice ({alice_total} gold)")
    else:
        print(f"Most valuable player: Bob ({bob_total} gold)")

    alice_count = sum(i['quantity'] for i in alice_inv.values())
    bob_count = sum(i['quantity'] for i in bob_inv.values())

    if alice_count > bob_count:
        print(f"Most items: Alice ({alice_count} items)")
    else:
        print(f"Most items: Bob ({bob_count} items)")

    rarest_items = []
    for inv in [alice_inv, bob_inv]:
        for name, details in inv.items():
            if (details['rarity'] in ['rare', 'legendary']
                    and name not in rarest_items):
                rarest_items.append(name)
    print(f"Rarest items: {', '.join(rarest_items)}")


if __name__ == '__main__':
    main()
