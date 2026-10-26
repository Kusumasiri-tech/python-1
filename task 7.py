stock = {"sandwich": 10, "juice": 8, "rice": 12}
prices = {"sandwich": 50, "juice": 25, "rice": 60}
daily_sales = 0

while True:
    item = input("Enter item name or 'done' to finish: ").lower()

    if item == "done":
        break
    elif item not in stock:
        print("Item not found.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Enter a quantity greater than zero.")
    elif quantity > stock[item]:
        print(f"Unavailable. Only {stock[item]} in stock.")
    else:
        bill = prices[item] * quantity
        stock[item] -= quantity
        daily_sales += bill
        print(f"Order bill: ₹{bill}")

print(f"\nDaily sales: ₹{daily_sales}")
print("Remaining stock:")
for item, quantity in stock.items():
    print(f"{item}: {quantity}")