# variable = a reusable container for storing a value
# Variable has a name, a type and a value

age = 21

print(age)
print("age")
print("I am age years old")

# string concatenation
print("I am" + age +"years old")

# type casting
# We can't add numbers to string

print("I am" + str(age) +"years old")

print("I am " + str(age) +" years old")

# separate arguments for print
print("I am", age, "years old")
# notice it includes space automatically.

# fstring
print(f"I am {age} years old")


# We learned about
# variables, string concatenation, separate arguments, fstring

# Data Types/ Variable Types
# Data type refers to the type of value a variable has and what type of mathematical, relational or logical operations can be applied
# The 4 basic data types are
# INTEGER
# FLOAT
# STRING
# BOOLEAN

# INTEGER
# Understand that anything which is a whole can be integer data type
age = 21
players = 2
quantity = 5
print(f"I am {age} years old.")
print(f"There are {players} online on Minecraft.")
print(f"I would like to buy {quantity} superhero characters.")

# FLOAT
# FLOAT is a number that contains decimal portion.
gpa = 3.2
distance = 2.5
price = 19.99

print(f"My gpa is {gpa}")
print(f"Today I ran {distance}Km")
print(f"The price of Python for Beginners book is ${price}")

# STRING
# Its just a series of characters withing a single ot double quotes.

name = "Shravan"
food = "pizza"
email = "shravan.jha@gmail.com"

print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is: {email}")

# BOOLEAN
# either true/false or binary. Consider its a kind of switch
# Example: If online it can be set to true else false

online = True
for_sale = False
running = True

print(f"Are you online:: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running: {running}")

if running:
    print("The game is running")
else:
    print("The game is over")
    
# Discuss if later in session.

# Common mistakes
#1 Make sure the boolean value is not in quotes else it will be considered as string
#2 Make sure The first letter us uppercase

# Multiple assignment

x = 1
y = 2
z = 3

# x, y, z = 1, 2, 3
# x = y = z = 0
print(x)
print(y)
print(x)

# Questions and Recaps