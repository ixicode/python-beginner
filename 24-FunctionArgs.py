# *args = parameters that will pack all arguments into a tuple
#       useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

print(add(0,1,2,3,4,5))

def add(*anything):
    sum = 0
    anything = list(anything)
    anything[0] = -1
    for i in anything:
        sum +=i
    return sum

print(add(0,1,2,3,4,5))