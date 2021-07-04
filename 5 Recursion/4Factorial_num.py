def print_factorial(n):
    if n==1:
        return 1
    fact=n*print_factorial(n-1)
    return fact # if we print directly fact here it is giving error but if we are returning fact it is working fine

n=int(input("enter the number"))
print(print_factorial(n))