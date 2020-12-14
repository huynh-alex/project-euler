sum = 0
for dividend in range(1000):
    if (dividend % 3 == 0) or (dividend % 5 == 0):
        sum += dividend
print(sum)