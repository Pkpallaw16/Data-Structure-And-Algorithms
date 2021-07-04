m1=int(input("eneter size of array"))
m2=int(input("eneter size of array"))
arr2=[[int(input()) for i in range(m2)] for j in range(m1)]
print(arr2)
for gap in range(m2):
    for row in range(m1-gap):
        col=row+gap
        print(arr2[row][col],end="->")