Problem statement
Allocate available emergency supplies to areas according to priority. Report any shortages, each area’s allocation and unmet demand, and the remaining stock.
Objectives
•	Allocate supplies in priority order.
•	Avoid allocating more than the available stock or requested amount.
•	Report shortages for each area.
•	Display allocations, unmet demand, and remaining stock.
Assumptions
•	A lower priority number means higher priority.
•	Stock quantities and supply needs are non-negative numbers.
•	Each area’s supplies are allocated before moving to the next area.
•	Supplies not listed in stock are treated as unavailable.
Algorithm
1.	Set the available stock and area requirements.
2.	Initialize every area’s allocation to zero.
3.	Process areas in priority order.
4.	For each requested supply, allocate the smaller of the amount needed and amount available.
5.	Subtract the allocation from stock and report any unmet demand.
6.	Display each area’s allocations and unmet demand.
7.	Display the remaining stock.
Testcase
Urgent shortage: South needs 20 more water.
Urgent shortage: South needs 10 more food.
Urgent shortage: South needs 15 more medicine.
Urgent shortage: East needs 30 more water.
Urgent shortage: East needs 25 more food.
Urgent shortage: East needs 20 more medicine.
Urgent shortage: East needs 10 more blankets.

Supply allocations

North:
  water: allocated 50, unmet demand 0
  food: allocated 40, unmet demand 0
  medicine: allocated 25, unmet demand 0
  blankets: allocated 20, unmet demand 0

South:
  water: allocated 50, unmet demand 20
  food: allocated 40, unmet demand 10
  medicine: allocated 15, unmet demand 15
  blankets: allocated 35, unmet demand 0

East:
  water: allocated 0, unmet demand 30
  food: allocated 0, unmet demand 25
  medicine: allocated 0, unmet demand 20
  blankets: allocated 5, unmet demand 10

Remaining stock
water: 0
food: 0
medicine: 0
blankets: 0
flowchart 
<img width="800" height="1341" alt="image" src="https://github.com/user-attachments/assets/9cee879d-8cde-49ef-abb1-54bf4f272114" />
 
Conclusion
The code distributes supplies by priority, tracks shortages for each area, and reports what remains in stock.
 <img width="940" height="498" alt="image" src="https://github.com/user-attachments/assets/35b152bd-5e41-4978-917f-59fc0166cf8c" />

