# Tuple = collection which is ordered and unchangeable
#       used to group together related data

student = ("Shravan", 41, "male")

print(student.count("Shravan"))
print(student.index("male"))

for x in student:
    print(x)
    
if "Shravan" in student:
    print("Shravan is here!")