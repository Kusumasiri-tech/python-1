Problem statement
Validate hackathon teams by size, calculate each valid team’s total and highest round score, then rank teams by total score, highest round score, and team name.
Objectives
•	Check whether each team meets the minimum and maximum size.
•	Calculate total and highest round scores for valid teams.
•	Rank valid teams using the specified tie-breakers.
•	Display the rankings and report invalid teams.
Assumptions
•	teams, minimum_team_size, maximum_team_size, and valid_teams are defined.
•	Each team has a name, student list, and round scores.
•	Round scores are numeric.
•	A higher total score ranks first; ties use highest round score, then team name alphabetically.
Algorithm
1.	For each team, count its students.
2.	If its size is within the allowed range, calculate its total and highest round score and add it to valid_teams.
3.	Otherwise, print that the team is invalid.
4.	Sort valid teams by total score descending, highest round score descending, and name alphabetically.
5.	Print the ranked teams and their scores.
Testcase
Input:
•	Minimum team size: 2
•	Maximum team size: 5

Hackathon Rankings
1. Team Beta | Students: 2 | Round scores: [92, 87, 89] | Total: 268 | Highest round: 92
2. Team Alpha | Students: 3 | Round scores: [85, 90, 88] | Total: 263 | Highest round: 90
3. Team Gamma | Students: 3 | Round scores: [85, 90, 88] | Total: 263 | Highest round: 90
flowchart 
<img width="940" height="1234" alt="image" src="https://github.com/user-attachments/assets/1b8a3ac7-c489-454d-889f-a223e8d44728" />

Conclusion
The code filters teams by size, scores eligible teams, and produces a ranking with consistent tie-breakers.
<img width="940" height="420" alt="image" src="https://github.com/user-attachments/assets/55025d0a-445b-432c-be88-9b7822321d5d" />
 
