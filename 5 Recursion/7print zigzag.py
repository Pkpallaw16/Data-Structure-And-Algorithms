def print_zigzag(n):
    if n==0:
        return
    #pre area
    print(n)
    print_zigzag(n-1)
    #in area
    print(n)
    print_zigzag(n-1)
    #post area
    print(n)

n=int(input("enter value of n"))
print_zigzag(n)