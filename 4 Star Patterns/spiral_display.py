m1=int(input("eneter size of array"))
m2=int(input("eneter size of array"))
arr2=[[int(input()) for i in range(m2)] for j in range(m1)]
minr=0
maxr=m1-1
minc=0
maxc=m2-1
count=0
while count<m1*m2:
    if count<m1*m2:
        for i in range(minr,maxr+1):
            print(arr2[i][minc],end=" ")
            count+=1
    minc+=1
    if count < m1 * m2:
        for i in range(minc,maxc+1):
            print(arr2[maxr][i],end=" ")
            count += 1
    maxr-=1
    if count < m1 * m2:
        for i in range(maxr,minr-1,-1):
            print(arr2[i][maxc],end=" ")
            count += 1
    maxc-=1
    if count < m1 * m2:
        for i in range(maxc,minc-1,-1):
            print(arr2[minr][i],end=" ")
            count += 1
    minr+=1
print()
print(arr2)