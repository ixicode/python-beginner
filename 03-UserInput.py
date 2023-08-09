# User input: It is used to accept user input from the same window where we see output of program.add()

# We assign input to a variable
name = input("Enter your name: ")
print(f"Hello {name}")

name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}")
print(f"Your are {age} years old")

age = input("Enter your age: ")
age = age +1
# Will this work?
print(f"Your are {age} years old")

age = input("Enter your age: ")
age = int(age)
age = age +1
print(f"Your are {age} years old")

# Can we shorten it?
age = int(input("Enter your age: "))
age = age +1
print(f"Your are {age} years old")

# try change it to float.

# Exercise 1: Create a mad libs game

adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f"Today I went to a {adjective1}  zoo.")
print(f"In a exhibit, I saw {noun}")
print(f"{noun} aws {adjective2} and {verb}ing")
print(f"I was {adjective3}")

# Exercise 2: Calculate the area of a rectangle and volume of cuboid

length = input("Enter the length of a rectangle in cm: ")
width = input("Enter the width of a rectangle in cm: ")

area = length * width
print(f"The area of the rectangle is: {area}cm^2")

# What is wrong here? Fir it.

length = float(input("Enter the length of a rectangle in cm: "))
width = float(input("Enter the width of a rectangle in cm: "))

area = length * width
print(f"The area of the rectangle is: {area}cm^2")

# Volume of a cuboid

length = float(input("Enter the length of a cuboid in cm: "))
width = float(input("Enter the width of a cuboid in cm: "))
height = float(input("Enter the height of a cuboid in cm: "))

volume = length * width * height
print(f"The volume of the cuboid is: {volume}cm^3")

# Exercise 3: Shopping cart

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f" You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total,2)}")