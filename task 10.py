slabs = [(100, 1.50), (300, 1.20), (float("inf"), 1.00)]
class_rates = {"Sleeper": 1.0, "AC": 2.0}
reservation_fee = 40
cancellation_penalty = 100

passengers = [
    {"name": "Asha", "age": 65, "distance": 250, "class": "AC"},
    {"name": "Ravi", "age": 30, "distance": 120, "class": "Sleeper"},
]

total = 0

for passenger in passengers:
    distance = passenger["distance"]
    rate = next(rate for limit, rate in slabs if distance <= limit)
    fare = distance * rate * class_rates[passenger["class"]]

    if passenger["age"] >= 60:
        fare *= 0.6

    fare += reservation_fee
    total += fare

    print(f"{passenger['name']}: ₹{fare:.2f}")

print(f"Total fare: ₹{total:.2f}")

cancel = input("Cancel reservation? (yes/no): ").lower()
if cancel == "yes":
    refund = max(0, total - cancellation_penalty * len(passengers))
    print(f"Refund after cancellation penalties: ₹{refund:.2f}")