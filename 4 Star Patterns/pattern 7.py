n=int(input("enter num"))
for r in range(1,n+1):
    for c in range(1,n+1):
       if r<=c:
           print("*",end=" ")
       else:
           print(" ",end=" ")
    print()

