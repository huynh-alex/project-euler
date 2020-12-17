import math

strValue = str(math.factorial(100))

sum = 0
for x in range(len(strValue)):
    sum += int(strValue[x])

print(sum)