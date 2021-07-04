n=int(input("enter num "))
nsp=int(n/2)
np=1
val=1
for i in range(1,n+1):
    for j in range(1,nsp+1):
        print(" ",end=" ")
    index=val
    for j in range(1,np+1):
        print(index, end=" ")
        if index<np:
            index+=1
        else:
            index-=1
    if i<=int(n/2):
        nsp-=1
        np+=2
        val+=1
    else:
        nsp+=1
        np-=2
        val-=1
    print()