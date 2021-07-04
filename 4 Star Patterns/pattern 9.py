n=int(input("enter num"))
lst=1
rst=n
for i in range(1,n+1):
    for j in range(1,n+1):
       if j==lst or j==rst:
           print("*",end=" ")
       else:
           print(" ",end=" ")
    lst+=1
    rst-=1
    print()


for r in range(1,n+1):
    for c in range(1,n+1):
        if r==c:
            print("*", end=" ")
        elif r+c==n+1:
            print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
print()

for r in range(1,n+1):
    for c in range(1,n+1):
        if r<=c and r+c<=n+1:
            print("*", end=" ")
        else:
           print(" ",end=" ")
    print()
print()
for r in range(1,n+1):
    for c in range(1,n+1):
        if r<=int(n/2) and r<=c and r+c<=n+1:
            print("*", end=" ")
        elif r>=c and r+c>=n+1:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


