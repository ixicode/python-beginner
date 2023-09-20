# **kwargs = parameter that will pack all arguments into a dictionary
#       useful so that function can accept a varying amount of keyword arguments

def hello(first, last):
    print("Hello "+ first + " " + last)
    
hello(first="Shravan", last = "Jha")
hello(first="Shravan", middle="Dude", last = "Jha")

def hello(**kwargs):
    print("Hello "+ kwargs['first'] + " " + kwargs['last'])
    # print("Hello", end=" ")
    # for key,value in kwargs.items():
    #     print(value, end=" ")
    
hello(first="Shravan", middle="Dude", last = "Jha")    
