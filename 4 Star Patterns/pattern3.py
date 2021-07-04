n=int(input("enter num "))
for i in range(n-1,-1,-1):
     for j in range(n):
         if j>=i:
             print("*",end=" ")
         else:
             print(" ",end=" ")
     print()


nst=1
nsp=n-1
for i in range(1,n+1):
    for j in range(1,nsp+1):
        print(" ",end=" ")
    for j in range(1,nst+1):
        print("*",end=" ")
    nst+=1
    nsp-=1
    print()
