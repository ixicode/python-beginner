# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti"]

print(food)
print(food[0])
# print(food[4])

food[0] = "Sushi"
print(food[0])

for x in food:
    print(x)

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0,"cake")
food.sort()
food.clear()

for x in food:
    print(x)