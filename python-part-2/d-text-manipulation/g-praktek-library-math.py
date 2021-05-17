import math

data = [2.22,-3.33,4.44,-5.55]
total = 0
for item in data:
    total += math.ceil(item)
print("Total: ", total)