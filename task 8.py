seats = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

tickets = ["ID101", "ID102", "ID103", "ID101", "ID105"]
registered_ids = ["ID101", "ID102", "ID103", "ID104", "ID105"]
used_ids = []

for ticket in tickets:
    if ticket not in registered_ids:
        print(f"{ticket}: invalid ticket")
    elif ticket in used_ids:
        print(f"{ticket}: duplicate entry")
    else:
        used_ids.append(ticket)

        assigned = False
        for row in range(len(seats)):
            for seat in range(len(seats[row])):
                if seats[row][seat] is None:
                    seats[row][seat] = ticket
                    print(f"{ticket}: Row {row + 1}, Seat {seat + 1}")
                    assigned = True
                    break
            if assigned:
                break

        if not assigned:
            print(f"{ticket}: no seats available")

available_seats = sum(
    seat is None for row in seats for seat in row
)

print(f"\nAvailable seats: {available_seats}")