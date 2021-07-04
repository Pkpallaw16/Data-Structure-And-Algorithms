n=int(input("enter num"))
nst=1
nsp=int(n/2)
flag=1
for i in range(1,n+1):
    for j in range(1,nsp+1):
        print(" ",end=" ")
    for j in range(1,nst+1):
        print("*",end=" ")
    if i<= int(n/2):
        nst+=2
        nsp-=1
    else:
        nst-=2
        nsp+=1
    print()

