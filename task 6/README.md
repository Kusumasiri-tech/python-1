Problem statement
A library has a limited stock of fiction, science, and history books. Several branches have different demands and priorities. Allocate books to branches in priority order, giving each branch as many copies of each book as possible from the remaining stock. Report the allocated copies, unmet demand, and final remaining stock.
Objective
To allocate available books to branches according to priority while tracking each branch’s unmet demand and the stock left afterward.
Assumptions
•	Lower priority numbers indicate higher priority.
•	Each branch’s demand is processed in the order listed: fiction, science, then history.
•	Books cannot be allocated beyond available stock.
•	Each branch’s demand is handled before moving to the next branch.
•	The stock dictionary contains all book categories requested by the branches.
Pseudocode
SET stock to the available copies of each book
SET branches to each branch's priority and demand

SORT branches by priority from lowest number to highest

FOR each branch in sorted branches
    DISPLAY branch name

    FOR each book and needed copies in that branch's demand
        allocated = minimum of needed copies and available stock
        subtract allocated copies from stock
        unmet = needed copies - allocated
        DISPLAY allocated copies and unmet demand
    END FOR
END FOR

DISPLAY remaining stock
Algorithm
1.	Initialize the available stock and branch demand data.
2.	Sort the branches by priority.
3.	For each branch in that order:
1.	Check each book’s demand against the remaining stock.
2.	Allocate the smaller of the demand and the available stock.
3.	Deduct the allocation from stock.
4.	Calculate unmet demand as demand minus allocation.
5.	Display the allocation and unmet demand.
4.	Display the remaining copies of each book.
Flowchart

<img width="940" height="1011" alt="image" src="https://github.com/user-attachments/assets/5bda3b99-fb1f-4b3e-ae2c-746f21799b3e" />

Conclusion
The program processes branches from highest to lowest priority and allocates available copies without exceeding the stock. Any demand that cannot be met is reported as unmet, and the final stock shows what remains after all branches have been processed.


<img width="940" height="499" alt="image" src="https://github.com/user-attachments/assets/a911f928-858c-40a6-b926-1a8e650c4831" />
