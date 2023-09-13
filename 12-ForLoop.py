# for loop = a statement that will execute it's block of code
#               a limited amount of time
#           while loop = unlimited
#           for loop = limited

for i in range(10):
    print(i+1)

for i in range(50,100):
    print(i)

for i in range(50,100,2):
    print(i)

for i in "Shravan Jha":
    print(i)
    
# Countdown

import time

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
