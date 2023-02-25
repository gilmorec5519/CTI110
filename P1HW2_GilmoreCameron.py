Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Calculate and Display Travel Expenses
... # Feb 25, 2023
... # CTI-110 P1HW2 - Travel Expense
... # Cameron Gilmore
... 
>>> print('This program calculates and displays travel expenses')
This program calculates and displays travel expenses
>>> budget = int(input('Enter Budget: '))
Enter Budget: 1200
>>> location = input('Enter your travel destination: ')
Enter your travel destination:  Nashville
>>> gas = int(input('How much will you spend on gas? '))
How much will you spend on gas? 250
>>> hotel = int(input('How much will you need for accomodation/hotel? '))
How much will you need for accomodation/hotel? 600
>>> food = int(input('How much will you need for food? '))
How much will you need for food? 300
>>> 
>>> # Output
>>> 
>>> print('-----------Travel Expenses----------')
-----------Travel Expenses----------
>>> print('Location: ', location)
Location:   Nashville
>>> print('Initial Budget: ', budget)
Initial Budget:  1200
>>> print('Fuel: ', gas)
Fuel:  250
>>> print('Accomodation: ', hotel)
Accomodation:  600
>>> print('Food: ', food)
Food:  300
>>> 
>>> sum1 = gas + hotel + food
>>> balance = budget - sum1
>>> print('Remaining Balance: ', balance)
Remaining Balance:  50
