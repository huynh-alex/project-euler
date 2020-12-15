finished = False
num = 20
divisor = 20

while(divisor > 0):
    if(num % divisor != 0):
        num += 20
        divisor = 20
    else:      
        divisor -= 1
    if(divisor == 1):
        print(num)