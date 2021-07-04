n=int(input("enter num"))
for r in range(1,n+1):
    for c in range(1,n+1):
       if r+c==n+1:
           print("*",end=" ")
           break
       else:
           print(" ",end=" ")
    print()


for r in range(1,n+1):
    for c in range(1,n+1):
       if r+c<=n+1:
           print("*",end=" ")

       else:
           print(" ",end=" ")
    print()

for r in range(1,n+1):
    for c in range(1,n+1):
       if r+c>=n+1:
           print("*",end=" ")

       else:
           print(" ",end=" ")
    print()

