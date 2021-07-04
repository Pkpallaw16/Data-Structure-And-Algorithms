def print_decreasing(n):
    if n==0:
        return
    print(n)
    print_decreasing(n-1)

def print_increasing(n):
    if n==0:
        return
    print_increasing(n-1)
    print(n)
def print_decreasing_increasing(n):
    if n==0:
        return
    print(n)
    print_decreasing_increasing(n-1)
    print(n)

n=int(input("enter the number"))
print_decreasing(n)
print_increasing(n)
print("print_decreasing_increasing")
print_decreasing_increasing(n)