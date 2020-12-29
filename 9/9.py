import math

def is_square(num):
    square_root = math.sqrt(num)
    return (square_root - int(square_root)) == 0

for a in range(500):
    for b in range(a+1, 500):
        c = math.sqrt(pow(a,2)+pow(b,2))
        if(is_square(pow(c,2)) and a + b + c == 1000):
            print(a * b * c)