m=int(input("eneter size of array"))
arr2=[[int(input()) for i in range(m)] for j in range(m)]
print(arr2)
for i in range(m):
    for j in range(i+1):
        arr2[i][j],arr2[j][i]=arr2[j][i],arr2[i][j]
print(arr2)
for i in range(m):
    left=0
    right=m-1
    while left<right:
        arr2[i][left],arr2[i][right]=arr2[i][right],arr2[i][left]
        left+=1
        right-=1
print(arr2)