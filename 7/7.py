import math

def isPrime(num):
    if(num == 1):
        return False
    if(num == 2):
        return True
    if(num % 2 == 0):
        return False
    divisor = 3
    while divisor < int(math.sqrt(num)+1):
        if(num % divisor == 0):
            return False
        divisor+=2
    return True

primeIndex = 0
num = 1

while primeIndex < 10002:
    if(isPrime(num)):
        #print(num)
        primeIndex+=1
        if(primeIndex == 10001):
            print(num)    
    num+=1