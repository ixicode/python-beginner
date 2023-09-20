# index operator [] = gives access to a sequence's element (str,list,tuples)

name = "shravan Jha"
if(name[0].islower()):
    name = name.capitalize()
print(name)

first_name = name[0:3].upper()
print(first_name)
#first_name = name[:3].upper()

last_name = name[4:].to.lower()
print(last_name)

last_character = name[-1]
print(last_character)
