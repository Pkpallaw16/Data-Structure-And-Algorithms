def reverse(arr,left,right):
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

def rotate(arr,k):
    k=k%len(arr)
    if k<0:
        k=k+len(arr)
    reverse(arr,0,len(arr)-k-1)
    reverse(arr,len(arr)-k,len(arr)-1)
    reverse(arr,0,len(arr)-1)
def set_oned_array(arr,s,oned_array):
    rows = len(arr)
    cols = len(arr[0])
    minr = s - 1
    maxr = rows - s
    minc = s - 1
    maxc = cols - s
    size = len(oned_array)
    idx = 0
    # left wall
    if idx < size:
        for r in range(minr, maxr+1):
            arr[r][minc]=oned_array[idx]
            idx += 1
        minc += 1
    # bottom wall
    if idx < size:
        for c in range(minc, maxc+1):
            arr[maxr][c]=oned_array[idx]
            idx += 1
        maxr -= 1
    # right wall
    if idx < size:
        for r in range(maxr, minr - 1,-1):
            arr[r][maxc]=oned_array[idx]
            idx += 1
        maxc -= 1
    # top wall
    if idx < size:
        for c in range(maxc, minc - 1,-1):
            arr[minr][c]=oned_array[idx]
            idx += 1
        minr += 1
def get_one_array(arr,s):
    rows=len(arr)
    cols=len(arr[0])
    minr = s-1
    maxr = rows-s
    minc = s-1
    maxc = cols-s
    size=2*(maxr-minr+maxc-minc)
    print(size)
    lis=[0 for i in range(size)]
    idx=0
    #left wall
    if idx<size:
        for r in range(minr,maxr+1):
            lis[idx]=arr[r][minc]
            idx+=1
        minc+=1
    # bottom wall
    if idx < size:
        for c in range(minc,maxc+1):
            lis[idx]=arr[maxr][c]
            idx+=1
        maxr-=1
    #right wall
    if idx < size:
        for r in range(maxr,minr-1,-1):
            lis[idx]=arr[r][maxc]
            idx+=1
        maxc-=1
    #top wall
    if idx < size:
        for c in range(maxc,minc-1,-1):
            lis[idx]=arr[minr][c]
            idx+=1
        minr+=1
    return lis
def rotateshell(arr,s,k):
    oned_array=get_one_array(arr,s)
    print(oned_array)
    rotate(oned_array,k)
    set_oned_array(arr,s,oned_array)


n=int(input("eneter size of array"))
m=int(input("eneter size of array"))
arr=[[int(input()) for i in range(m)] for j in range(n)]
print(arr)
shell=int(input("enter shell number"))
k=int(input("number of rotation "))
rotateshell(arr,shell,k)
print(arr)