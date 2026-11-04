TASK – 5
Problem statement
Distribute available books to library branches in priority order. Show how many copies each branch receives, any unmet demand, and the remaining stock.
Objectives
•	Allocate books to branches by priority.
•	Keep allocations within available stock and branch demand.
•	Report unmet demand and remaining copies.
Assumptions
•	A lower priority number means higher priority.
•	Stock and demand values are non-negative whole numbers.
•	Each branch receives books before the next branch is processed.
Algorithm
1.	Set the book stock and branch demands.
2.	Process branches in priority order.
3.	For each requested book, allocate the smaller of the demand and available stock.
4.	Update stock and calculate unmet demand.
5.	Display each branch’s allocations and the remaining copies.
Testcase
Central
fiction: allocated 8, unmet demand 0
science: allocated 6, unmet demand 0
history: allocated 4, unmet demand 0

East
fiction: allocated 10, unmet demand 0
science: allocated 5, unmet demand 0
history: allocated 6, unmet demand 0

West
fiction: allocated 2, unmet demand 5
science: allocated 1, unmet demand 3
history: allocated 0, unmet demand 3

Remaining copies: {'fiction': 0, 'science': 0, 'history': 0}
Flowchart
<img width="730" height="1454" alt="image" src="https://github.com/user-attachments/assets/44075d6f-34ca-4e55-bed1-926965b1b72f" />
     
Conclusion
The program allocates books by branch priority, tracks unmet demand, and shows the stock left after distribution.
 <img width="940" height="499" alt="image" src="https://github.com/user-attachments/assets/d8922adc-3b70-46fd-a77d-13b912b30f13" />

