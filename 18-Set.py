# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}

# utensils = {"fork", "spoon", "knife", "knife"}

for x in utensils:
    print(x)

utensils.add("napkins")
utensils.remove("fork")
utensils.clear()

for x in utensils:
    print(x)
    
dishes = {"bowl", "plate", "cup"}    
utensils.update(dishes)

for x in utensils:
    print(x)

dinner_table = utensils.union(dishes)
for x in dinner_table:
    print(x)    
    
print(utensils.difference(dishes))
print(utensils.intersection(dishes))