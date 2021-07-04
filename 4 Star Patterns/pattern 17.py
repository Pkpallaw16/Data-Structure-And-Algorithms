n=int(input("enter numer"))
star=1
space=int(n/2)
for r in range(n):
    if r==int(n/2):
        for st in range(int(n/2)):
            print("*", end=" ")
    else:
        for sp in range(space):
            print(" ", end=" ")
    for st in range(star):
        print("*",end=" ")
    print()

    if r<int(n/2):
        star+=1
    else:
        star-=1
