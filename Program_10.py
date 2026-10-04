store1 = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}
store2 = {
    "Laptop": 5,
    "Mouse": 10,
    "Monitor": 8
}
store3 = {
    "Laptop": 3,
    "Keyboard": 7,
    "Monitor": 4
}

def merge_inventory(*stores):
    inventory = {}

    for store in stores:
        for item, quantity in store.items():
            if item in inventory:
                inventory[item] += quantity
            else:
                inventory[item] = quantity

    return inventory

total_inventory = merge_inventory(store1, store2, store3)

print("Total Inventory:")
print(total_inventory)

print("\nMouse Stock:", total_inventory.get("Mouse", 0))
print("Printer Stock:", total_inventory.get("Printer", 0))

item = "Monitor"

if item in total_inventory:
    print("\n", item, "is available.")
else:
    print("\n", item, "is not available.")

low_stock = {
    item: quantity
    for item, quantity in total_inventory.items()
    if quantity < 10
}

print("\nLow Stock Items:")
print(low_stock)

new_store = {
    "Laptop": 2,
    "Printer": 6
}

for item, quantity in new_store.items():
    total_inventory[item] = total_inventory.get(item, 0) + quantity

print("\nInventory After Adding New Store:")
print(total_inventory)