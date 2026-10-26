minimum_team_size = int(input("Enter minimum team size: "))
maximum_team_size = int(input("Enter maximum team size: "))

teams = [
    {
        "name": "Team Alpha",
        "students": ["Asha", "Ravi", "Neha"],
        "rounds": [85, 90, 88],
    },
    {
        "name": "Team Beta",
        "students": ["Maya", "Arun"],
        "rounds": [92, 87, 89],
    },
    {
        "name": "Team Gamma",
        "students": ["Kiran", "Isha", "Dev"],
        "rounds": [85, 90, 88],
    },
]

valid_teams = []

for team in teams:
    team_size = len(team["students"])

    if minimum_team_size <= team_size <= maximum_team_size:
        team["total_score"] = sum(team["rounds"])
        team["highest_round_score"] = max(team["rounds"])
        valid_teams.append(team)
    else:
        print(f'{team["name"]} is invalid: team size is {team_size}.')

ranked_teams = sorted(
    valid_teams,
    key=lambda team: (
        -team["total_score"],
        -team["highest_round_score"],
        team["name"].lower(),
    ),
)

print("\nHackathon Rankings")

for rank, team in enumerate(ranked_teams, start=1):
    print(
        f"{rank}. {team['name']} | "
        f"Students: {len(team['students'])} | "
        f"Round scores: {team['rounds']} | "
        f"Total: {team['total_score']} | "
        f"Highest round: {team['highest_round_score']}"
    )