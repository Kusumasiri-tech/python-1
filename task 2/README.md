TASK – 2:
Problem statement
Create a program to calculate the cost of an event, total funds from participant registrations and sponsorship, and whether the event has a surplus or shortfall. It also calculates the minimum registrations needed to break even, when each registration covers its per-participant costs.
Objectives
•	Calculate fixed and variable event costs.
•	Calculate total event cost.
•	Calculate registration contributions and sponsorship funds.
•	Report the event’s surplus or funding shortfall.
•	Find the minimum registrations needed to cover remaining fixed costs.
Assumptions
•	All cost and funding amounts are entered in INR.
•	Expected participants is a non-negative whole number.
•	Registration fees and sponsorship are applied as entered.
•	Each registration pays the same fee and incurs the same catering and certificate costs.
•	Break-even registrations are calculated against fixed costs remaining after sponsorship.
Algorithm
1.	Get the event costs, expected participants, registration fee, and sponsorship amount.
2.	Add venue, equipment, and transport costs to find fixed costs.
3.	Multiply per-participant catering and certificate costs by expected participants to find variable costs.
4.	Add fixed and variable costs to get total event cost.
5.	Calculate registration contributions and add sponsorship to get total funds.
6.	Compare funds with total cost and report a surplus or shortfall.
7.	If the registration fee exceeds per-participant costs:
o	Subtract sponsorship from fixed costs.
o	Calculate the minimum registrations needed to cover the remaining fixed cost.
8.	Otherwise, report that break-even through registrations is not possible.
      Testcase
Input:
•	Registration fee per participant in INR: 1000
•	Sponsorship amount in INR: 3000

Fixed costs: ₹29000.00
Variable costs: ₹270000.00
Total event cost: ₹299000.00
Participant contributions: ₹600000.00
Sponsorship: ₹3000.00
Surplus: ₹304000.00
Minimum registrations to break even: 48
Flowchart
 <img width="858" height="1454" alt="image" src="https://github.com/user-attachments/assets/c4ee58c0-8da2-410b-8114-22cfe25764ec" />

Conclusion
The program summarizes event costs and available funding, reports any surplus or shortfall, and estimates the registrations needed to break even when each registration contributes toward fixed costs.
 <img width="940" height="496" alt="image" src="https://github.com/user-attachments/assets/56283d51-64d0-4321-a621-bd677f2be095" />

