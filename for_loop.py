"""
Question 1 — For Loop
Write a Python program to print numbers from 1 to 5 using a for loop.
"""
# for num in range(1,6):
#     print(num)

"""
Question 2 — For Loop
Write a Python program to print: Hello
5 times using a for loop.
"""
# for char in range(5):
#     print("Hello")

"""
Question - 3 Write a Python program to print numbers from 1 to 10 using a for loop.
"""
# for i in range(1,11):
#     print(i)

"""
Question - 4 Write a Python program to print all even numbers from 1 to 10 using a for loop.
"""
# for i in range(1,11):
#     if i%2==0:
#         print(i)

""" 
Question 5 — For Loop
Write a Python program to print all odd numbers from 1 to 20 using a `for` loop.
"""
# for i in range(1,21):
#     if i%2!=0:
#         print(i)

"""
# Question 6 — For Loop
Write a Python program to print the multiplication table of 5 using a `for` loop.
"""
# for i in range(1, 11):
#     print("5 *", i, "=", 5 * i)

"""
# Question 7 — For Loop
Write a Python program to calculate the sum of numbers from 1 to 10 using a `for` loop.
"""
# total = 0
# for i in range(1,11):
#     total = total + i
# print("Sum is",total)

"""
# Question 8 — For Loop
Write a Python program to print the square of numbers from 1 to 10 using a `for` loop.
"""
# for i in range(1,11):
#     print(i**2)

"""
# Question 9 — For Loop
Write a Python program to print numbers from 10 to 1 using a `for` loop.
"""
# for i in range(10,0,-1):
#     print(i)

"""
# Question 10 — For Loop
Write a Python program to print the multiplication table of a number entered by the user using a `for` loop.
"""
# num = int(input("Enter number: "))

# for i in range(1,11):
#     result = num * i
#     print(result)

"""
# Question 11 — For Loop
Write a Python program to count how many even numbers are present from 1 to 20 using a `for` loop.
"""
# count = 0
# for i in range(1,21):
#     if i%2==0:
#         count = count+1
# print("Total even numbers are",count)

"""
# Question 12 — For Loop
Write a Python program to print all numbers from 1 to 50 that are divisible by 3 using a `for` loop.
"""
# for i in range(1,51):
#     if i%3==0:
#         print(i)

"""
# Question 13 — For Loop
Write a Python program to print the cube of numbers from 1 to 10 using a `for` loop.
"""
# for i in range(1,11):
#     print(i**3)

"""
# Project Question 1 — ATM System with Multiple Transactions
Write a Python program for an ATM system.
The program should:
* Take account balance as input
* Use a `for` loop 3 times
* Each time ask for withdraw amount
* If withdraw amount is less than or equal to balance:

  * Deduct amount from balance
  * Print remaining balance
* Otherwise:

  * Print `"Insufficient balance"`
At the end, print final account balance.
"""
# balance = float(input("Enter account balance: "))

# for i in range(3):

#     withdraw_amount = float(input("Enter withdraw amount: "))

#     if withdraw_amount <= balance:
#         balance = balance - withdraw_amount
#         print("Remaining balance is", balance)

#     else:
#         print("Insufficient balance")

# print("Final account balance is", balance)

"""
# Project Question 2 — Shopping Bill
Create a program where:
* User enters how many products they bought
* Then user enters price of each product one by one
* Program should calculate total bill
After that:
* If total bill is 5000 or more:
  * Print `"Discount applied"`
* Otherwise:
  * Print `"No discount"`
Finally print total bill amount 
"""
# products = int(input("Enter number of products: "))

# total_bill = 0

# for i in range(products):

#     price = float(input("Enter product price: "))

#     total_bill = total_bill + price

# if total_bill >= 5000:
#     print("Discount applied")

# else:
#     print("No discount")

# print("Your final total bill is", total_bill)

"""
# Project Question 3 — Student Attendance System
Create a program where:
* User enters total number of classes
* User enters number of attended classes
* Program calculates attendance percentage
Conditions:
* If attendance is 75% or more:
  * Print `"Allowed in exam"`
* Otherwise:
  * Print `"Not allowed in exam"`
Also print attendance percentage 
"""
# total_classes = int(input("Enter number of classes:"))
# attended_classes = int(input("Enter number of attended classes:"))
# attendance_percentage = attended_classes/total_classes*100

# if attendance_percentage >= 75:
#     print("Allowed in exam")
# else:
#     print("Not allowed in exam")

# print("Your attendance percentage is",attendance_percentage)

"""
# Project Question 4 — Mobile Recharge History System
Create a program where:
* User enters how many recharges they did
* Use a `for` loop to enter recharge amount one by one
* Program should calculate total recharge amount
Conditions:
* If total recharge amount is greater than or equal to 1000:
  * Print `"Gold customer"`
* Otherwise:
  * Print `"Regular customer"`
Also print total recharge amount 
"""
# recharges = int(input("Enter number of recharges: "))

# total_amount = 0

# for i in range(recharges):

#     recharge_amount = float(input("Enter recharge amount: "))

#     total_amount = total_amount + recharge_amount

# if total_amount >= 1000:
#     print("Gold customer")

# else:
#     print("Regular customer")

# print("Your total recharge amount is", total_amount)

"""
# Project Question 5 — Grocery Shopping System
Create a program where:
* User enters how many grocery items they bought
* Use a `for` loop to enter price of each item
* Program should calculate total grocery bill
Conditions:
* If total bill is greater than or equal to 3000:
  * Print `"Big shopper"`
* Else if total bill is greater than or equal to 1500:
  * Print `"Medium shopper"`
* Otherwise:
  * Print `"Small shopper"`
Also print total grocery bill 🙂
"""
# grocery_items = int(input("Enter number of grocery items:"))

# total_price = 0
# for i in range(grocery_items):
#     price = float(input("Enter price of each item:"))
#     total_price = total_price + price

# if total_price >= 3000:
#     print("Big shopper")
# elif total_price >= 1500:
#     print("Medium shopper")
# else:
#     print("Small shopper")
# print("Your total grocery bill is",total_price)
    
"""
# Project Question 6 — Electricity Bill System
Create a program where:
* User enters how many months electricity bill they want to add
* Use a `for` loop to enter bill amount month by month
* Program should calculate total electricity bill
Conditions:
* If total bill is greater than or equal to 5000:
  * Print `"High electricity usage"`
* Else if total bill is greater than or equal to 2500:
  * Print `"Medium electricity usage"`
* Otherwise:
  * Print `"Low electricity usage"`
Also print total electricity bill 
"""
# electricity_bill = int(input("Enter number of months electricity bill:"))
# bill_amount = 0

# for i in range(electricity_bill):
#     bill = float(input("Enter bill amount:"))
#     bill_amount = bill_amount + bill

# if bill_amount >= 5000:
#     print("High electricity usage")
# elif bill_amount >= 2500:
#     print("Medium electricity usage")
# else:
#     print("Low electricity usage")

# print("Your total electricity bill is",bill_amount)

"""
# Project Question 7 — Online Course Fee System
Create a program where:
* User enters how many courses they purchased
* Use a `for` loop to enter fee of each course
* Program should calculate total course fee
Conditions:
* If total fee is greater than or equal to 10000:
  * Print `"Premium student"`
* Else if total fee is greater than or equal to 5000:
  * Print `"Standard student"`
* Otherwise:
  * Print `"Basic student"`
Also print total course fee 
"""
# courses_purchased = int(input("Enter number of courses:"))

# total_course_fee = 0

# for i in range(courses_purchased):
#     total_fee = float(input("Enter fee of each course"))
#     total_course_fee = total_course_fee + total_fee

# if total_course_fee >= 10000:
#     print("Premium student")
# elif total_course_fee >= 5000:
#     print("Standard student")
# else:
#     print("Basic student")
  
# print("Your total course fee is",total_course_fee)

"""
# Project Question 8 — Cab Fare Collection System
Create a program where:
* User enters how many rides they completed
* Use a `for` loop to enter fare of each ride
* Program should calculate total earnings
Conditions:
* If total earnings are greater than or equal to 10000:
  * Print `"Top Driver"`
* Else if total earnings are greater than or equal to 5000:
  * Print `"Active Driver"`
* Otherwise:
  * Print `"Beginner Driver"`
Also print total earnings 
"""
# rides = int(input("Enter number of rides:"))
# total_earnings = 0
# for i in range(rides):
#     ride_fare = float(input("Enter fare of each ride"))
#     total_earnings = total_earnings + ride_fare

# if total_earnings >= 10000:
#     print("Top driver")
# elif total_earnings >= 5000:
#     print("Active driver")
# else:
#     print("Beginner driver")

# print("Your total earning is",total_earnings)

"""
# Project Question 9 — Daily Water Intake Tracker
Create a program where:
* User enters how many days they tracked water intake
* Use a `for` loop to enter liters of water drank each day
* Program should calculate total water intake
Conditions:
* If total water intake is greater than or equal to 20:
  * Print `"Excellent hydration"`
* Else if total water intake is greater than or equal to 10:
  * Print `"Good hydration"`
* Otherwise:
  * Print `"Drink more water"`
Also print total water intake 
"""
# tracked_water_intake = int(input("Enter tracked water intake:"))
# total_water_intake = 0

# for i in range(tracked_water_intake):
#     water_drank = float(input("Enter liters of water drank each day"))
#     total_water_intake = total_water_intake + water_drank

# if total_water_intake >= 20:
#     print("Excellent hydration")
# elif total_water_intake >= 10:
#     print("Good hydration")
# else:
#     print("Drink more water")

# print("You drank total water intake is",total_water_intake)

"""
# Project Question 10 — Mobile Data Usage System
Create a program where:
* User enters how many days mobile data was used
* Use a `for` loop to enter data usage (in GB) for each day
* Program should calculate total data usage
Conditions:
* If total data usage is greater than or equal to 50:
  * Print `"Heavy data user"`
* Else if total data usage is greater than or equal to 20:
  * Print `"Average data user"`
* Otherwise:
  * Print `"Light data user"`
Also print total data usage 
"""
# mobile_data_used = int(input("Enter days mobile data was used:"))
# total_data = 0

# for i in range(mobile_data_used):
#     data_usage = float(input("Enter data used for each day"))
#     total_data = total_data + data_usage

# if total_data >= 50:
#     print("Heavy data user")
# elif total_data >= 20:
#     print("Average data user")
# else:
#     print("Light data user")

# print("Your total data usage is",total_data,"GB")

"""
# Project Question 11 — Online Food Order System
Create a program where:
* User enters how many food items they ordered
* Use a `for` loop to enter price of each food item
* Program should calculate total food bill
Conditions:
* If total food bill is greater than or equal to 3000:
  * Print `"Free dessert"`
* Else if total food bill is greater than or equal to 1500:
  * Print `"Free cold drink"`
* Otherwise:
  * Print `"No free item"`
Also print total food bill
"""
# food_items = int(input("Enter food items:"))
# total_food_bill = 0

# for i in range(food_items):
#     food_price = float(input("Enter price of each food item"))
#     total_food_bill = total_food_bill + food_price

# if total_food_bill >= 3000:
#     print("Free dessert")
# elif total_food_bill >= 1500:
#     print("Free cold drink")
# else:
#     print("No free item")

# print("Your total food bill is",total_food_bill)

"""
# Project Question 12 — Monthly Savings Tracker
Create a program where:
* User enters how many months they saved money
* Use a `for` loop to enter savings amount for each month
* Program should calculate total savings
Conditions:
* If total savings are greater than or equal to 50000:
  * Print `"Excellent saving habit"`
* Else if total savings are greater than or equal to 20000:
  * Print `"Good saving habit"`
* Otherwise:
  * Print `"Need to save more"`
Also print total savings 
"""
# month_saved_money = int(input("Enter months saved money:"))
# total_savings = 0

# for i in range(month_saved_money):
#     savings_amount = float(input("Enter savings amount for each month"))
#     total_savings = total_savings + savings_amount

# if total_savings >= 50000:
#     print("Excellent saving habit")
# elif total_savings >= 20000:
#     print("Good saving habit")
# else:
#     print("Need to save more")

# print("Your total savings amount is",total_savings)    
    
"""
# Project Question 13 — Daily Exercise Tracker
Create a program where:
* User enters how many days they exercised
* Use a `for` loop to enter exercise hours for each day
* Program should calculate total exercise hours
Conditions:
* If total exercise hours are greater than or equal to 20:
  * Print `"Fitness Champion"`
* Else if total exercise hours are greater than or equal to 10:
  * Print `"Good Fitness Routine"`
* Otherwise:
  * Print `"Need More Exercise"`
Also print total exercise hours 
"""
# exercised_days = int(input("Enter days exercised:"))
# total_exercise_hours = 0

# for i in  range(exercised_days):
#     exercise_hours = float(input("Enter exercise hours for each day"))
#     total_exercise_hours = total_exercise_hours + exercise_hours

# if total_exercise_hours >= 20:
#     print("Fitness Champion")
# elif total_exercise_hours >= 10:
#     print("Good Fitness Routine")
# else:
#     print("Need More Exercise")

# print("Total exercise hours is",total_exercise_hours)

"""
# Project Question 14 — Online Book Store System
Create a program where:
* User enters how many books they purchased
* Use a `for` loop to enter price of each book
* Program should calculate total book bill
Conditions:
* If total bill is greater than or equal to 4000:
  * Print `"Book Lover Premium Member"`
* Else if total bill is greater than or equal to 2000:
  * Print `"Book Lover"`
* Otherwise:
  * Print `"New Reader"`
Also print total book bill 
"""
# books_purchased = int(input("Enter number of books they purchased:"))
# total_book_bill = 0

# for i in range(books_purchased):
#     book_price = float(input("Enter price of book"))
#     total_book_bill = total_book_bill + book_price

# if total_book_bill >= 4000:
#     print("Book Lover Premiun Member")
# elif total_book_bill >= 2000:
#     print("Book Lover")
# else:
#     print("New Reader")
# print("Your total book price is",total_book_bill)

"""
# Project Question 15 — Travel Expense Tracker
Create a program where:
* User enters how many trips they made
* Use a `for` loop to enter expense of each trip
* Program should calculate total travel expense
Conditions:
* If total expense is greater than or equal to 20000:
  * Print `"Luxury Traveler"`
* Else if total expense is greater than or equal to 10000:
  * Print `"Frequent Traveler"`
* Otherwise:
  * Print `"Budget Traveler"`
Also print total travel expense 
"""
# trips = int(input("Enter number of trips"))
# total_travel_expense = 0

# for i in range(trips):
#     expense_each_trip = float(input("Enter expense of trip"))
#     total_travel_expense = total_travel_expense + expense_each_trip

# if total_travel_expense >= 20000:
#     print("Luxury Traveler")
# elif total_travel_expense >= 10000:
#     print("Frequent Traveler")
# else:
#     print("Budget Traveler")
# print("Total travel expense is",total_travel_expense)

