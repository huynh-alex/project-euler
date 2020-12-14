import math

num = 600851475143

#reduce number to be odd, as all even factors indicate primeness
while num % 2 == 0:
    num /= 2

divisor = 3
#property of prime factors of numbers is that no prime factor is larger than the root of the number
while divisor < int(math.sqrt(num)):
    #if it can divide, reduce it continuously
    if num % divisor == 0:
        while(num % divisor == 0):
            num /= divisor
    divisor +=2
print(num)