 Problem statement
Create a program that converts travel expenses into INR, adds a conversion fee, compares total spending with a budget, and identifies the largest expense category.
Objectives
•	Convert expenses from foreign currencies to INR.
•	Add a conversion fee to each expense.
•	Calculate total spending and category totals.
•	Compare spending with the budget.
•	Identify the largest category.
Assumptions
•	Exchange rates are given as INR per unit of foreign currency.
•	The fee applies to each converted expense.
•	Budget and fee inputs are valid numbers.
•	Amounts are rounded for display to two decimal places.
Algorithm
1.	Set the exchange rates and expense list.
2.	Ask for the budget and fee percentage.
3.	For each expense, check whether its currency has an exchange rate.
4.	Convert valid expenses to INR and add the fee.
5.	Update category totals and total spending.
6.	Compare total spending with the budget.
7.	Display the largest expense category.
Test case
Input:
•	Budget in INR: 50000
•	Conversion fee percentage: 20

       Accommodation: 500.00 EUR = ₹54000.00
Food: 300.00 USD = ₹29800.00
Transport: 20000.00 JPY = ₹13440.00
Activities: 180.00 GBP = ₹22680.00

Total spending: ₹120000.00
Budget: ₹50000.00
Over budget by ₹70000.00
Largest category: Accommodation (₹54000.00)


Flowchart
 <img width="680" height="1454" alt="image" src="https://github.com/user-attachments/assets/2dcc4b0e-c3ef-491f-87fa-69c753d37187" />

Conclusion
The program helps track travel spending in INR, including conversion fees, and shows whether the expenses fit within the budget.

 <img width="940" height="393" alt="image" src="https://github.com/user-attachments/assets/73c2363a-7a07-4f19-8727-da1e3100855a" />


