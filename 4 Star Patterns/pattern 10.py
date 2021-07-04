n=int(input("enter number"))
row=n
n-=1
for r in range(row):
    for c in range(row):
        if r+c==n/2 or c-r==n/2 or r-c==n/2 or r+c==3*n/2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()