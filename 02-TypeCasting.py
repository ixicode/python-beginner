# typecasting - The process of converting a value of one data type to another
# (string, integer, float, boolean)
# (str, int, float, bool)


# Why we learn about it?
# user input is always a string so we will need to convert it to right data type
# We might need to round off and convert data from float to integer 

name = "Shravan"
age = 21
gpa = 1.9
student = True

# How to know the data type of a variable?
# Use type() function
# type(name)

print (type(name))
print (type(age))
print (type(gpa))
print (type(student))

# convert a variable value to another data type and reassign it to the same variable
age = float(age)

print(age)
print (type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

student = str(student)
print(student)
print(type(student))

# What would happen when we convert an integer to boolean?
age = bool(age)
print(age)
print(type(age))

# When can it be true? try it out.

#1 age = 0
#2 name = ""

# Explicit vs Implicit. 
# Explicit means than you manually convert one data type to another using keywords
# Implicit when a value of a variable is converted to different data type automatically.

x = 2
y = 2.0

x = x / y

# What will be the data type of x now?

print(x)
print(type(x))
# Note: The data type of a has been automatically converted to float from int after the above operation