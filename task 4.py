stock = {
    "water": 100,
    "food": 80,
    "medicine": 40,
    "blankets": 60,
}

requirements = {
    "North": {
        "priority": 1,
        "supplies": {"water": 50, "food": 40, "medicine": 25, "blankets": 20},
    },
    "South": {
        "priority": 2,
        "supplies": {"water": 70, "food": 50, "medicine": 30, "blankets": 35},
    },
    "East": {
        "priority": 3,
        "supplies": {"water": 30, "food": 25, "medicine": 20, "blankets": 15},
    },
}

allocations = {
    area: {supply: 0 for supply in stock}
    for area in requirements
}

for area, details in sorted(
    requirements.items(),
    key=lambda item: item[1]["priority"],
):
    for supply, needed in details["supplies"].items():
        available = stock.get(supply, 0)
        allocated = min(needed, available)

        allocations[area][supply] = allocated
        stock[supply] = available - allocated

        unmet = needed - allocated
        if unmet > 0:
            print(f"Urgent shortage: {area} needs {unmet} more {supply}.")

print("\nSupply allocations")

for area, details in requirements.items():
    print(f"\n{area}:")
    for supply, needed in details["supplies"].items():
        allocated = allocations[area][supply]
        unmet = needed - allocated
        print(
            f"  {supply}: allocated {allocated}, "
            f"unmet demand {unmet}"
        )

print("\nRemaining stock")
for supply, quantity in stock.items():
    print(f"{supply}: {quantity}")