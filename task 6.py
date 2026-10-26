stock = {"fiction": 20, "science": 12, "history": 10}

branches = {
    "Central": (1, {"fiction": 8, "science": 6, "history": 4}),
    "East": (2, {"fiction": 10, "science": 5, "history": 6}),
    "West": (3, {"fiction": 7, "science": 4, "history": 3}),
}

for branch, (priority, demand) in sorted(
    branches.items(),
    key=lambda item: item[1][0],
):
    print(f"\n{branch}")

    for book, needed in demand.items():
        allocated = min(needed, stock.get(book, 0))
        stock[book] -= allocated
        unmet = needed - allocated
        print(f"{book}: allocated {allocated}, unmet demand {unmet}")

print("\nRemaining copies:", stock)