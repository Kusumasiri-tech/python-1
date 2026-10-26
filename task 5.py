events = [
    ("Football", "09:00", "10:30", "Team A", 3),
    ("Basketball", "09:00", "10:00", "Team B", 2),
    ("Volleyball", "10:45", "11:45", "Team A", 1),
    ("Swimming", "12:00", "13:00", "Team C", 3),
    ("Tennis", "10:15", "11:15", "Team B", 2),
]

team_points = {}

print("Scheduling conflicts")

for i in range(len(events)):
    for j in range(i + 1, len(events)):
        event_1 = events[i]
        event_2 = events[j]

        if event_1[1] < event_2[2] and event_2[1] < event_1[2]:
            print(f"{event_1[0]} and {event_2[0]} overlap.")

for event in events:
    event_name, start_time, end_time, team, points = event
    team_points[team] = team_points.get(team, 0) + points

rankings = sorted(
    team_points.items(),
    key=lambda item: (-item[1], item[0]),
)

print("\nFinal rankings")

for rank, (team, points) in enumerate(rankings, start=1):
    print(f"{rank}. {team}: {points} points")