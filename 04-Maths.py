# This session covers
# Arithmetic operators
# math functions
# exercises

friends = 5

# Addition
friends = friends + 1

print(friends)

# Augmented assignment operators
friends += 1
print(friends)

# Subtraction
friends = friends - 2
friends -= 2
print(friends)


# Multiplication
friends = friends * 3
friends *= 3


# Division
friends = friends / 2
friends /= 2

# Power
friends = friends ** 2
friends **= 2

# Modulus
# Check if you have end or odd number odd friends

remainder = friends % 3
print(remainder)

print(friends)

# Build In function

x = 3.14
y = 4
z = 5

# round to nearest whole number
result = round(x)
# returns the absolute value
result = abs(y)
# calculate power
result = pow(4,3)
# calculate max and min value 
result = max(x, y, z)
result = min(x, y, z)

print(result)

# Using match library

import math

print(math.pi)
print(math.e)

x = 9
result = math.sqrt(x)

# round a number up
result = math.ceil(x)
# round a number down
result = math.floor(x)

# Exercise: circumference of a circle
# c = 2 * PI * r
import math

radius = float(input('Enter the radius of a circle in cm: '))
circumference = 2 * math.pi * radius

print(f"The circumference of the circle is: {circumference}cm")


# Exercise: area of a circle
# a = PI * r * r
import math

radius = float(input('Enter the radius of a circle in cm: '))
area = math.pi * pow(radius,2)

print(f"The area of the circle is: round{round(area,2)}cm^2")

# Exercise: area of a circle
# a = PI * r * r
import math

radius = float(input('Enter the radius of a circle in cm: '))
area = math.pi * pow(radius,2)

print(f"The area of the circle is: {round(area,2)}cm^2")


# Exercise: hypotenuse of a right angle triangle
# c = Square root(a*a + b*b)
import math

a = float(input('Enter side A in cm: '))
b = float(input('Enter side B in cm: '))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse of a right angle triangle: {c}cm")