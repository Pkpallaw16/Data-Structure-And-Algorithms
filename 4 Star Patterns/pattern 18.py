n=int(input("enter numer"))
for r in range(n):
    for c in range(n):
        if r<=int(n/2):
            if r==c or r+c==n-1 or r==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            if r>c and r+c>n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()

