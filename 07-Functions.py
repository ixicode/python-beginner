# Function = A block of reusable code.
# Place () after the function name to invoke it
# It has input arguments and return type
# def FunctionName(input1, input2)

print("Happy birthday to you!")
print("You are old!")
print("Happy birthday to you!")
print()

# Define
def happy_birthday():
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

# Invoke
happy_birthday()
happy_birthday()

# Arguments
def happy_birthday(name):
    print("Happy birthday to {name}!")
    print("You are old!")
    print("Happy birthday to you!")
    print()
happy_birthday("Joe")
happy_birthday("Steve")

# Multiple Arguments 
# sequence is important while passing arguments

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()
happy_birthday("Joe", 12)
happy_birthday("Steve", 13)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("JoeBiden", 100.10, "01/01/2024")

# Return = statement used to end a function 
# and send the result back to caller

def add(x,y):
    z = x + y
    return z
def subtract(x,y):
    z = x - y
    return z
def multiply(x,y):
    z = x * y
    return z
def divide(x,y):
    z = x / y
    return z
print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last - last.capitalize()
    return first + " " + last

full_name = create_name("Shravan", "Jha")
print(full_name)
