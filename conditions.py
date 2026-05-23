"""
# Question 1 Write a Python program to take a user's age as input and check whether the person is eligible to vote or not.

Condition:
* Age 18 or above → Eligible to vote
* Otherwise → Not eligible to vote.
"""
age = int(input("Enter your age:"))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

"""
# Question 2 Write a Python program to take a number as input and check whether the number is positive or negative.
Condition:
* Number greater than 0 → Positive number
* Otherwise → Negative number.
"""
num = float(input("Enter number:"))
if num > 0:
    print("Positive number")
else:
    print("Negative number")

"""
# Question 3 Write a Python program to take a number as input and check whether the number is even or odd.
Condition:
* Number divisible by 2 → Even number
* Otherwise → Odd number.
"""
num = int(input("Enter number:"))
if num%2==0:
    print("Number is even")
else: 
    print("Number is odd")

"""
# Question 4 Write a Python program to take a user's password as input and check whether the password is correct or not.
Condition:
* If password is `"python123"` → Login successful
* Otherwise → Incorrect password.
"""
password = str(input("Enter your correct password:"))
if password == "python123":
    print("Login successful")

else:
    print("Incorrect Password")

"""
# Question 5 Write a Python program to take a student's marks as input and check whether the student is pass or fail.
Condition:
* Marks 33 or above → Pass
* Otherwise → Fail.
"""
marks = float(input("Enter marks:"))
if marks >= 33:
    print("Pass")
else:
    print("Fail")

"""
# Question 6 Write a Python program to take two numbers as input and print the greater number.
Condition:
* If first number is greater → print first number
* Otherwise → print second number.
"""
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

if a>b:
    print(a)
else:
    print(b)

"""
# Question 7 Write a Python program to take a user's age as input and check:
* If age is 18 or above → Adult
* Otherwise → Minor.
"""
age = int(input("Enter your age:"))
if age >= 18:
    print("You are Adult")
else:
    print("You are Minor")

"""
# Question 8 Write a Python program to take a user's username as input and check:
* If username is `"admin"` → Access granted
* Otherwise → Access denied.
"""
username = str(input("Enter username:"))
if username == "admin":
    print("Access granted")
else:
    print("Access denied")

"""
# Question 9 Write a Python program to take a number as input and check:
* If the number is greater than 100 → Print `"Big number"`
* Otherwise → Print `"Small number"`
"""
number = float(input("Enter number:"))
if number > 100:
    print("Big number")
else:
    print("Small number")

"""
# Question 10 Write a Python program to take a temperature as input and check:
* If temperature is greater than 30 → Print `"Hot weather"`
* Otherwise → Print `"Normal weather"`
"""
temperature = float(input("Enter temperature:"))
if temperature > 30:
    print("Hot weather")
else:
    print("Normal weather")

"""
# Question 11 Write a Python program to take a user's balance as input and check:
* If balance is greater than or equal to 1000 → Print `"Transaction successful"`
* Otherwise → Print `"Insufficient balance"`
"""
balance = float(input("Enter balance:"))
if balance >=1000:
    print("Transaction successful")
else:
    print("Insufficient balance")

"""
# Question 12 Write a Python program to take a user's exam percentage as input and check:
* If percentage is greater than or equal to 75 → Print `"Distinction"`
* Otherwise → Print `"No Distinction"`
"""
percentage = float(input("Enter your percentage:"))
if percentage >= 75:
    print("Distinction")
else:
    print("No Distinction")

"""
# Question 13 Write a Python program to take a user's speed as input and check:
* If speed is greater than 80 → Print `"Overspeeding"`
* Otherwise → Print `"Normal speed"`
"""
speed = int(input("Enter speed:"))
if speed > 80:
    print("Overspeeding")
else:
    print("Normal speed")

"""
# Question 14 Write a Python program to take a user's shopping amount as input and check:
* If amount is greater than or equal to 5000 → Print `"Discount applied"`
* Otherwise → Print `"No discount"`
"""
shopping_amount = float(input("Enter shopping amount:"))
if shopping_amount >= 5000:
    print("Discount applied")
else:
    print("No discount")

"""


# Question 15 Write a Python program to take a user's electricity bill amount as input and check:
* If bill amount is greater than 2000 → Print `"High electricity bill"`
* Otherwise → Print `"Normal electricity bill"`
"""
electricity_amount = float(input("Enter electricity amount:"))

if electricity_amount > 2000:
    print("High electricity bill")
else:
    print("Normal electricity bill")

"""
# Question 16 Write a Python program for an ATM withdrawal system.
The program should:
* Take account balance as input
* Take withdraw amount as input
* If withdraw amount is less than or equal to balance → Print `"Withdrawal successful"`
* Otherwise → Print `"Insufficient balance"`
"""
balance = float(input("Enter account balance:"))
withdraw_amount = float(input("Enter withdraw amount:"))

if withdraw_amount <= balance:
    print("Withdrawl Successful")
else:
    print("Insufficient balance")

"""
# Question 17 — Login System
Write a Python program for a login system.
The program should:
* Take username as input
* Take password as input
Conditions:
* If username is `"admin"` and password is `"python123"`:
  * Print `"Login successful"`
* Otherwise:
  * Print `"Invalid username or password"`
"""
username = str(input("Enter username:"))
password = str(input("Enter password:"))

if username == "admin" and password == "python123":
    print("Login successful")
else:
    print("Invalid username or password")

"""
# Question 18 — Online Food Delivery System
Write a Python program for an online food delivery system.
The program should:
* Take order amount as input
Conditions:
* If order amount is greater than or equal to 500:
  * Print `"Free delivery available"`
* Otherwise:
  * Print `"Delivery charges applied"`
"""
food_amount = int(input("Enter amount:"))
if food_amount >= 500:
    print("Free delivery available")
else:
    print("Delivery charges applied")

"""
# Question 19 — Online Shopping Discount System
Write a Python program for an online shopping discount system.
The program should:
* Take shopping amount as input
Conditions:
* If shopping amount is greater than or equal to 3000:
  * Print `"20% discount applied"`
* Otherwise:
  * Print `"No discount available"`
"""
shopping_amount = float(input("Enter shopping amount:"))
if shopping_amount >= 3000:
    print("20% discount applied")

else:
    print("No discount available")

"""
# Question 20 — Movie Ticket Booking System
Write a Python program for a movie ticket booking system.
The program should:
* Take the number of tickets as input
* Take the price of one ticket as input
* Calculate total amount
Conditions:
* If total amount is greater than or equal to 1000:
  * Print `"You got a free popcorn"`
* Otherwise:
  * Print `"No free popcorn"`
Also print the total bill amount.
"""
number_tickets = int(input("Enter number of tickets:"))
price_ticket = float(input("Enter price of one ticket:"))

total_amount = number_tickets * price_ticket
if total_amount >= 1000:
    print("You got a free popcorn")
else:
    print("No free popcorn")
print("Your total bill amount is",total_amount)

"""
# Question 21 — Cab Booking System

Write a Python program for a cab booking system.

The program should:
* Take travel distance in kilometers as input
* Calculate fare:
  * ₹15 per kilometer
Conditions:
* If total fare is greater than or equal to 500:
  * Print `"Premium ride"`
* Otherwise:
  * Print `"Normal ride"`
Also print the total fare amount.
"""
kilometers = float(input("Enter travel distance in Kilometers:"))
total_fare = kilometers*15
if total_fare >= 500:
    print("Premium ride")
else:
    print("Normal ride")
print("Your total amount of travelling is",total_fare)

"""
# Question 22 — Restaurant Billing System
Write a Python program for a restaurant billing system.
The program should:
* Take food bill amount as input
* Calculate service charge:
  * 5% of food bill
Conditions:
* If total bill is greater than or equal to 2000:
  * Print `"VIP Customer"`
* Otherwise:
  * Print `"Regular Customer"`
Also print:
* Service charge
* Final bill amount.
"""
foodbill_amount = float(input("Enter food bill amount:"))
service_charge = 0.05*foodbill_amount
total_bill = foodbill_amount + service_charge

if total_bill >= 2000:
    print("VIP customer")
else:
    print("Regular customer")

print("Your service charge of total bill is",service_charge)
print("Your final bill including service charge is",total_bill)

"""
# Question 23 — Student Grade System
Write a Python program for a student grade system.
The program should:
* Take student's marks as input
Conditions:
* If marks are greater than or equal to 90:
  * Print `"Grade A"`
* Else if marks are greater than or equal to 75:
  * Print `"Grade B"`
* Else if marks are greater than or equal to 50:
  * Print `"Grade C"`
* Otherwise:
  * Print `"Fail"`
"""
marks = float(input("Enter students marks:"))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

"""
# Question 24 — ATM Menu System
Write a Python program for an ATM menu system.
The program should:
* Take a number as input
Conditions:
* If number is `1`:
  * Print `"Check Balance"`
* Else if number is `2`:
  * Print `"Withdraw Money"`
* Else if number is `3`:
  * Print `"Deposit Money"`
* Otherwise:
  * Print `"Invalid Option"`
"""
number = int(input("Enter number:"))
if number == 1:
    print("Check balance")
elif number == 2:
    print("Withdraw money")
elif number == 3:
    print("Deposit Money")
else:
    print("Invalid option")

"""
# Question 25 — Traffic Light System
Write a Python program for a traffic light system.
The program should:
* Take traffic light color as input
Conditions:
* If color is `"red"`:
  * Print `"Stop"`
* Else if color is `"yellow"`:
  * Print `"Get Ready"`
* Else if color is `"green"`:
  * Print `"Go"`
* Otherwise:
  * Print `"Invalid traffic light color"`
"""
traffic_light_color = str(input("Enter traffic light color:"))
if traffic_light_color == "red":
    print("Stop")
elif traffic_light_color == "yellow":
    print("Get ready")
elif traffic_light_color == "green":
    print("Go")
else:
    print("Invalid traffic light color")

"""
# Question 26 — Mobile Recharge Plan System
Write a Python program for a mobile recharge plan system.
The program should:
* Take recharge amount as input
Conditions:
* If recharge amount is `199`:
  * Print `"1GB/day plan activated"`
* Else if recharge amount is `399`:
  * Print `"2GB/day plan activated"`
* Else if recharge amount is `599`:
  * Print `"Unlimited 5G plan activated"`
* Otherwise:
  * Print `"Invalid recharge amount"`
"""
recharge_amount = float(input("Enter recharge amount:"))

if recharge_amount == 199:
    print("1GB/day plan activated")
elif recharge_amount == 399:
    print("2GB/day plan activated")
elif recharge_amount == 599:
    print("Unlimited 5G plan activated")
else:
    print("Invalid recharge amount")

"""
# Question 27 — Simple Calculator System
Write a Python program for a simple calculator system.
The program should:
* Take first number as input
* Take second number as input
* Take operator as input (`+`, `-`, `*`, `/`)
Conditions:
* If operator is `+`:
  * Print addition
* Else if operator is `-`:
  * Print subtraction
* Else if operator is `*`:
  * Print multiplication
* Else if operator is `/`:
  * Print division
* Otherwise:
  * Print `"Invalid operator"`
"""
num1 = float(input("Enter fisrt number:"))
num2 = float(input("Enter second number:"))
operator = input("Enter operator (+,-,*,/):")

if operator == "+":
    print("Addition is",num1+num2)
elif operator == "-":
    print("Subtraction is",num1-num2)
elif operator == "*":
    print("Multiplication is",num1*num2)
elif operator == "/":
    print("Division is",num1/num2)
else:
    print("Invalid operator")

"""
# Question 28 — Online Course Platform
Write a Python program for an online course platform.
The program should:
* Take course name as input
Conditions:
* If course name is `"python"`:
  * Print `"Python course enrolled"`
* Else if course name is `"java"`:
  * Print `"Java course enrolled"`
* Else if course name is `"web development"`:
  * Print `"Web Development course enrolled"`
* Otherwise:
  * Print `"Course not available"`
"""
course_name = str(input("Enter course name:"))

if course_name == "python":
    print("Python course enrolled")
elif course_name == "java":
    print("Java course enrolled")
elif course_name == "web development":
    print("Web development course enrolled")
else:
    print("Course not available")

"""
# Question 29 — Weather Suggestion System
Write a Python program for a weather suggestion system.
The program should:
* Take weather condition as input
Conditions:
* If weather is `"rainy"`:
  * Print `"Take an umbrella"`
* Else if weather is `"sunny"`:
  * Print `"Wear sunglasses"`
* Else if weather is `"cold"`:
  * Print `"Wear a jacket"`
* Otherwise:
  * Print `"Weather condition unknown"`
"""
weather = str(input("Enter weather condition:"))
if weather == "rainy":
    print("Take an umbrella")
elif weather == "sunny":
    print("Wear sunglasses")
elif weather == "cold":
    print("Wear a jacket")
else:
    print("Weather condition unknown")

"""
# Question 30 — Online Payment System
Write a Python program for an online payment system.
The program should:
* Take payment method as input
Conditions:
* If payment method is `"upi"`:
  * Print `"Payment through UPI"`
* Else if payment method is `"card"`:
  * Print `"Payment through Card"`
* Else if payment method is `"cash"`:
  * Print `"Cash payment selected"`
* Otherwise:
  * Print `"Invalid payment method"`
"""
payment_method = str(input("Enter payment method:"))
if payment_method == "upi":
    print("Payment through UPI")
elif payment_method == "card":
    print("Payment through Card")
elif payment_method == "cash":
    print("Cash payment selected")
else:
    print("Invalid payment method")

"""
# Question 31 — E-commerce Delivery System
Write a Python program for an e-commerce delivery system.
The program should:
* Take delivery type as input
Conditions:
* If delivery type is `"standard"`:
  * Print `"Delivery in 5 days"`
* Else if delivery type is `"express"`:
  * Print `"Delivery in 2 days"`
* Else if delivery type is `"same day"`:
  * Print `"Delivery today"`
* Otherwise:
  * Print `"Invalid delivery type"`
"""
delivery = str(input("Enter delivery type:"))
if delivery == "standard":
    print("Delivery in 5 days")
elif delivery == "express":
    print("Delivery in 2 days")
elif delivery == "same day":
    print("Delivery today")
else:
    print("Invalid delivery type")

"""
# Question 32 — Smart Phone Battery System
Write a Python program for a smart phone battery system.
The program should:
* Take battery percentage as input
Conditions:
* If battery percentage is greater than or equal to 80:
  * Print `"Battery is full"`
* Else if battery percentage is greater than or equal to 40:
  * Print `"Battery is medium"`
* Else if battery percentage is greater than or equal to 10:
  * Print `"Battery is low"`
* Otherwise:
  * Print `"Charge your phone immediately"`
"""
battery_percentage = float(input("Enter battery percentage:"))
if battery_percentage >= 80:
    print("Battery is full")
elif battery_percentage >= 40:
    print("Battery is medium")
elif battery_percentage >= 10:
    print("Battery is low")
else:
    print("Charge your phone immediately")

"""
# Question 33 — Online Exam Result System
Write a Python program for an online exam result system.
The program should:
* Take percentage as input
Conditions:
* If percentage is greater than or equal to 90:
  * Print `"Excellent"`
* Else if percentage is greater than or equal to 75:
  * Print `"Very Good"`
* Else if percentage is greater than or equal to 50:
  * Print `"Good"`
* Otherwise:
  * Print `"Need Improvement"`
"""

percentage = float(input("Enter percentage"))
if percentage >= 90:
    print("Excellent")
elif percentage >= 75:
    print("Very Good")
elif percentage >= 50:
    print("Good")
else:
    print("Need Improvement")

"""
# Question 34 — Gym Membership System
Write a Python program for a gym membership system.
The program should:
* Take membership type as input
Conditions:
* If membership type is `"silver"`:
  * Print `"Access to gym only"`
* Else if membership type is `"gold"`:
  * Print `"Access to gym and swimming pool"`
* Else if membership type is `"platinum"`:
  * Print `"All facilities available"`
* Otherwise:
  * Print `"Invalid membership type"`
"""
membership = str(input("Enter membership type:"))
if membership == "silver":
    print("Access to gym only")
elif membership == "gold":
    print("Access to gym and swimming pool")
elif membership == "platinum":
    print("All facilities available")
else:
    print("Invalid membership type")

"""
# Question 35 — Train Ticket Booking System
Write a Python program for a train ticket booking system.
The program should:
* Take class type as input
Conditions:
* If class type is `"sleeper"`:
  * Print `"Sleeper class booked"`
* Else if class type is `"ac"`:
  * Print `"AC class booked"`
* Else if class type is `"general"`:
  * Print `"General class booked"`
* Otherwise:
  * Print `"Invalid class type"`
"""
class_type = str(input("Enter class type:"))
if class_type == "sleeper":
    print("Sleeper class booked")
elif class_type == "ac":
    print("AC class booked")
elif class_type == "general":
    print("General class booked")
else:
    print("Invalid class type")/

