sum = 0
for i in range(1, 1001):
    sum += pow(i,i)

stringed = str(sum)
print(sum)
print(stringed[-10:])