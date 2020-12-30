def fac(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

def ncr(n, r):
    return fac(n) / ((fac(r))*fac(n-r))

def ncrUpto(n):
    vals = 0
    for i in range(1,n+1):
        for j in range(1, i):
            result = ncr(i,j)
            if result > 1000000:
                vals+=1
    return vals

print(ncr(23,10))