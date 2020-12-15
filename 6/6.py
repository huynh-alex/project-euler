sumSquares = 0
for i in range(101):
    sumSquares += i * i

preSquaredSum = 0
squaredSum = 0
for i in range(101):
    preSquaredSum += i
squaredSum = preSquaredSum*preSquaredSum

print(squaredSum - sumSquares)