# What is slicing?
# String slicing = Create a substring by extracting elements from another string
#           indexing[] [start:stop:step] 
#           or slice(start,stop,step)
name = "Shravan Jha"

first_letter = name[0]
print(first_letter)

first_name = name[0:7]
print(first_name)

last_name = name[8:]
print(last_name)

funky_name = name[0:11:2] # [::2] #
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)

website1 = "https://ixicode.com"
website2 = "https://google.com"
slice = slice(8,-4)

print(website1[slice])
print(website2[slice])
