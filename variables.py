#Q-1 Sum of two numbers
a = 10
b = 20
sum = a+b
print(sum)

# # #Q-2 print Username
name = str(input("Enter your name:"))
print("Hello",name)

# #Q-3 Area of rectangle
length = 5
breadth = 6
area = length*breadth
print(area)

# # #Q-4 Area of Circle
radius = 7
pi = 3.14
area = pi*radius*radius
print(area)

# #Q-5 Swap two variables3

a = 5
b = 10
a,b = b,a
print(a)
print(b)

# #Q-6 Celsius to Fahrenhit

celsius = 25
fahrenhit = (9/5*celsius)+32
print(fahrenhit)

# #Q-7 Simple Interest

p  = 1000
r = 5
t = 2

si = (p*r*t)/100
print(si)

# #Q-8 Avearge of three numbers

a=10
b=20
c=30
average = (a+b+c)/3
print(average)

# #Q-9 Square of a number

num = 6
square = num**2
print(square)


# #Q-10 Cube of a number
num = 2
cube = num**3
print(cube)

# #Q-11 Age AFter 5 years
age = 18
future_age = age+5
print(future_age)

# #Q-12 Kilometer to meter conversion

km = 5
meter = km*1000
print(meter)

# #Q-13 Student Details
name = "Shreya"
age = 21
course = "python"
print(name)
print(age)
print(course)

# #Q-14 Total marks
maths = 80
science = 75
english = 90
total = maths + science + english
print(total)

# #Q-15 Salary bonus

salary = 50000
bonus = salary*0.10
print(bonus)

#Q-16 multiplication of two numbers
a = 2
b = 6
multiplication = a*b
print(multiplication)

#Q-17 Store a mobile brand name
brand = "Samsung"
print("I use", brand, "mobile.")

#Q-18 Store your favourite food in a variable
food = "Burger"
print("My favourite food is",food)

#Q-19 Store your College name in a variable
college = "Vidhyadeep University"
print("My college name is",college)

#Q-20 WAP to take users name and age as input 
name = str(input("Enter name:"))
age = int(input("Enter age"))
print("My name is", name, "and I am",age,"years old")

#Q-21 WAP to take two numbers as input from the user and print their addition, subtraction, multiplication and division

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
sum = a+b
print("Sum is:",sum)

subtraction = a-b
print("Subtraction is:",subtraction)

multiplication = a*b
print("Multiplication is:",multiplication)

division = a/b
print("Division is:",division)

#Q-22 WAP to take the price of a product and quantity as input and calculate the total bill

price = int(input("Enter price:"))
qty = int(input("Enter quantity:"))

total_bill = price*qty
print("Your total bill is",total_bill)

"""
Q-23 Write a Python program to take the basic salary 
of an employee as input and calculate:
HRA = 20% of salary
Bonus = 10% of salary
Total Salary = salary + HRA + Bonus
"""
salary = int(input("Enter your basic salary:"))
HRA = salary*0.20
Bonus = salary*0.10
Total_salary = salary + HRA + Bonus
print("Your total salary will be",Total_salary)

"""
Q-24 Write a Python program to take the marks of 5 subjects as input and calculate:
Total Marks
Average Marks
Then print both results.
"""

math = int(input("Enter maths marks:"))
english = int(input("Enter english marks:"))
hindi = int(input("Enter hindi marks:"))
science = int(input("Enter science marks:"))
gujarati = int(input("Enter gujarati marks:"))

total_marks = math + english + hindi + science + gujarati
print("Total marks:",total_marks)

average_marks = (total_marks)/5
print("Average of all subjects:",average_marks)

"""
Q- 25 Write a Python program to take the radius of a circle as input and calculate:
Area of the circle
Circumference of the circle
Use:
π = 3.14
"""
radius = float(input("Enter radius of a circle:"))
pi = 3.14
Area_circle = pi*radius*radius
print("Area of the circle:",Area_circle)

Circumference_circle = 2*pi*radius
print("Circumference of the circle:",Circumference_circle)

"""
Q - 26 Write a Python program to take the length and width of a rectangle as input and calculate:
Area of rectangle
Perimeter of rectangle.
"""
length = int(input("Enter length of a rectangle:"))
width = int(input("Enter width of a rectangle:"))

Area_rectangle = length*width
print("Area of rectangle:",Area_rectangle)

Perimeter_rectangle = 2*(length + width)
print("Perimeter of rectangle:",Perimeter_rectangle)

"""
Q- 27 Write a Python program for a simple ATM system.
The program should:

Take the user's balance as input
Take the withdraw amount as input
Calculate the remaining balance
Print the remaining balance
"""
balance = int(input("Enter balance:"))
withdraw_amount = int(input("Enter withdraw amount:"))

remaining_balance = balance - withdraw_amount
print("The remaining balance is",remaining_balance)

"""
Q- 28 Write a Python program for a movie ticket booking system.

The program should:
* Take the ticket price as input
* Take the number of tickets as input
* Calculate the total amount
* Print the final bill amount.
"""
ticket_price = float(input("Enter ticket price:"))
qty_ticket = int(input("Enter number of ticket:"))

total_amount = ticket_price * qty_ticket
print("The total amount of ticket is",total_amount)
print("Thank you & Visit again")

"""
Q - 29 Write a Python program for a food ordering system.

The program should:
* Take the food item name as input
* Take the price of one item as input
* Take the quantity as input
* Calculate the total bill
* Print the food item name and total bill amount.
"""
food_name = str(input("Enter food name:"))
price_food = int(input("Enter price of one item:"))
qty_food = int(input("Enter quantity of food:"))

total_bill = price_food * qty_food
print("The total bill of your food is",total_bill)
print("You buy the",food_name,"and total bill of your food is",total_bill)

"""
Q - 30 Write a Python program for a mobile recharge system.

The program should:
* Take the mobile number as input
* Take the recharge amount as input
* Print a successful recharge message with the mobile number and recharge amount.
"""
mobile_number = int(input("Enter your mobile number:"))
recharge_amount = float(input("Enter your recharge amount:"))

print("Recharge of", recharge_amount, "for mobile number", mobile_number, "was successful.")


"""
Q - 31 Write a Python program for a shopping bill system.

The program should:
* Take the product name as input
* Take the product price as input
* Take the quantity as input
* Calculate GST as 18% of total amount
* Calculate the final bill
* Print the product name, GST amount, and final bill.
"""
product_name = str(input("Enter your product name:"))
product_price = float(input("Enter your product price:"))
qty_product = int(input("Enter quantity of product:"))

amount = product_price * qty_product
gst = amount * 0.18

total_amount = amount + gst
print("Your final bill is",total_amount)
print("Your product:",product_name,"GST amount:",gst,"And your final bill was",total_amount)