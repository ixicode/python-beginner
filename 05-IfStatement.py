# If = execute some code only if some condition is True
#           Else do something else

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
#################

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
else:
    print("You must be 18+ to sign up")

################

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't born yet!")
elif age >= 100:
    print("You are too old to sign up!")    
else:
    print("You must be 18+ to sign up")
    
# Try to organize above statements in correct order.    

if age >= 100:
    print("You are too old to sign up!") 
if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't born yet!")
elif age >= 100:
    print("You are too old to sign up!")    
else:
    print("You must be 18+ to sign up")

####################
    
response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

###################

name = input("Enter your name: ")    

if name == "":
    print("You did not type in your name!")
else:
    print(f" Hello {name}")
    
###################

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")
    
#############

online = False

if online:
    print("The user is online")
else:
    print("The user is offline")