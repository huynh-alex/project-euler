def isPalindrome(num):
    stringNum = str(num)
    for i in range(len(stringNum)):
        if stringNum[i] != stringNum[len(stringNum)-i-1]:
            return False
    return True

max = 0
for i in range(1000):
    for j in range(1000):
        product = i*j
        if(isPalindrome(product) and product > max):
            max = product

print(max)