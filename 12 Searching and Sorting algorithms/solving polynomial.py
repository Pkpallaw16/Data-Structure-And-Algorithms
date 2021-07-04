import math
def solve_polynomial(x,n):
    a=n
    p=1
    poly=0
    for i in range(1,n+1):
        p=p*x
        poly+=a*p
        a-=1
    print(poly)
solve_polynomial(2,2)