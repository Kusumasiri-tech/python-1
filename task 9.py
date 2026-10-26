matches = [
    ("Lions", "Tigers", 2, 1),
    ("Eagles", "Lions", 1, 1),
    ("Tigers", "Eagles", 3, 0),
]

scores = {}

for team1, team2, goals1, goals2 in matches:
    for team in (team1, team2):
        if team not in scores:
            scores[team] = {"points": 0, "difference": 0}

    scores[team1]["difference"] += goals1 - goals2
    scores[team2]["difference"] += goals2 - goals1

    if goals1 > goals2:
        scores[team1]["points"] += 3
    elif goals2 > goals1:
        scores[team2]["points"] += 3
    else:
        scores[team1]["points"] += 1
        scores[team2]["points"] += 1

rankings = sorted(
    scores.items(),
    key=lambda item: (-item[1]["points"], -item[1]["difference"], item[0]),
)

for rank, (team, result) in enumerate(rankings, start=1):
    print(f"{rank}. {team}: {result['points']} points, "
          f"tie-break value {result['difference']}")