# Variable scope = The region a variable is recognized
#           A variable is only available inside the region it created
#           Global variable vs local variables

name = "Shravan Jha" # global variable (available inside and outside of functions)

def display_name():
    name = "Jha" # Local variable only available inside a function
    print(name)

display_name()
print(name)