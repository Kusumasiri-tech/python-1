venue_cost = float(input("Enter venue cost in INR: "))
equipment_cost = float(input("Enter equipment cost in INR: "))
catering_cost_per_person = float(input("Enter catering cost per participant in INR: "))
transport_cost = float(input("Enter transport cost in INR: "))
certificate_cost_per_person = float(input("Enter certificate cost per participant in INR: "))
expected_participants = int(input("Enter expected number of participants: "))
registration_fee = float(input("Enter registration fee per participant in INR: "))
sponsorship_amount = float(input("Enter sponsorship amount in INR: "))

fixed_costs = venue_cost + equipment_cost + transport_cost
variable_costs = (
    catering_cost_per_person + certificate_cost_per_person
) * expected_participants
total_cost = fixed_costs + variable_costs

participant_contributions = registration_fee * expected_participants
total_funds = participant_contributions + sponsorship_amount

print(f"\nFixed costs: ₹{fixed_costs:.2f}")
print(f"Variable costs: ₹{variable_costs:.2f}")
print(f"Total event cost: ₹{total_cost:.2f}")
print(f"Participant contributions: ₹{participant_contributions:.2f}")
print(f"Sponsorship: ₹{sponsorship_amount:.2f}")

if total_funds >= total_cost:
    print(f"Surplus: ₹{total_funds - total_cost:.2f}")
else:
    shortfall = total_cost - total_funds
    print(f"Funding shortfall: ₹{shortfall:.2f}")
if registration_fee > catering_cost_per_person + certificate_cost_per_person:
    contribution_per_participant = (registration_fee- catering_cost_per_person- certificate_cost_per_person)
    remaining_cost = fixed_costs - sponsorship_amount
    if remaining_cost <= 0:
        minimum_registrations = 0
    else:
        minimum_registrations = int(
            (remaining_cost + contribution_per_participant - 1)
            // contribution_per_participant
        )

    print(f"Minimum registrations to break even: {minimum_registrations}")
else:
    print("Break-even is not possible: each registration does not cover its variable costs.")