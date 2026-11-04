TASK – 8
Problem statement
Validate event tickets, prevent duplicate entries, assign valid tickets to the first available seat, and report how many seats remain.
Objectives
•	Reject tickets that are not registered.
•	Prevent a ticket from being used more than once.
•	Assign valid tickets to available seats.
•	Count and display remaining seats.
Assumptions
•	Seats are assigned row by row, from left to right.
•	Each ticket ID can be used once.
•	The seating layout is fixed at three rows with three seats each.
Algorithm
1.	Create the seating grid and ticket lists.
2.	For each ticket, check whether it is registered and unused.
3.	If valid, mark it as used and assign the first empty seat.
4.	Report invalid tickets, duplicate entries, or a full seating area.
5.	Count and display available seats.
Testcase
Expected output:
ID101: Row 1, Seat 1
ID102: Row 1, Seat 2
ID103: Row 1, Seat 3
ID104: duplicate entry
ID105: Row 2, Seat 1

Available seats: 5

flowchart 

<img width="594" height="1454" alt="image" src="https://github.com/user-attachments/assets/cba383ec-bce1-456f-a813-26daa29cdb10" />


Conclusion

<img width="940" height="494" alt="image" src="https://github.com/user-attachments/assets/fbad311b-837e-4731-9b62-7bd96372e2fe" />

The program checks each ticket, assigns seats in order, prevents duplicate entries, and reports remaining capacity.
 
