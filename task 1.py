home_currency = "INR"

exchange_rates = {
    "INR": 1.00,
    "USD": 83.00,
    "EUR": 90.00,
    "GBP": 105.00,
    "JPY": 0.56,
}

budget = float(input("Enter your budget in INR: "))
fee_percent = float(input("Enter conversion fee percentage: "))
fee_rate = fee_percent / 100

expenses = [
    ("Accommodation", "500", "EUR"),
    ("Food", "300", "USD"),
    ("Transport", "20000", "JPY"),
    ("Activities", "180", "GBP"),
]

category_totals = {}
total_spending = 0.0

for category, amount_text, currency in expenses:
    amount = float(amount_text)

    if currency in exchange_rates:
        converted_amount = amount * exchange_rates[currency]
        amount_with_fee = converted_amount * (1 + fee_rate)

        category_totals[category] = (
            category_totals.get(category, 0.0) + amount_with_fee
        )
        total_spending += amount_with_fee

        print(
            f"{category}: {amount:.2f} {currency} "
            f"= ₹{amount_with_fee:.2f}"
        )
    else:
        print(f"Skipping {category}: no exchange rate for {currency}")

print(f"\nTotal spending: ₹{total_spending:.2f}")
print(f"Budget: ₹{budget:.2f}")

if total_spending > budget:
    print(f"Over budget by ₹{total_spending - budget:.2f}")
elif total_spending == budget:
    print("You spent exactly your budget.")
else:
    print(f"Under budget by ₹{budget - total_spending:.2f}")

if category_totals:
    largest_category = max(category_totals, key=category_totals.get)
    print(
        f"Largest category: {largest_category} "
        f"(₹{category_totals[largest_category]:.2f})"
    )
else:
    print("No expenses had valid exchange rates.")