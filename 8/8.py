num = ""
max = 0

#read in file
file = open("8/8.txt", "r")
for line in file:
    num += line[:-1]
num += "0"

for i in range(len(num)-13):
    product = 1
    for j in range(i, i+13):
        product *= ord(num[j]) - 48 #ASCII conversion
    if product > max:
        max = product

print(max)