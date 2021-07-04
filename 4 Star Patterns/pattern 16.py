n=int(input("enter numer"))
star=1
space=2*n-3
for r in range(1,n+1):
    for st in range(1,star+1):
        print("*",end=" ")
    for sp in range(1,space+1):
        print(" ",end=" ")
    if r==n:
        star-=17

    for st in range(1,star+1):
        print("*",end=" ")
    print()
    star+=1
    space-=2

star=1
space=2*n-3
for r in range(1,n+1):
    val=1
    for st in range(1,star+1):
        print(val,end=" ")
        val+=1
    for sp in range(1,space+1):
        print(" ",end=" ")
    if r==n:
        star-=1
        val -= 1

    for st in range(1,star+1):
        val -= 1
        print(val,end=" ")

    print()
    star+=1
    space-=2
