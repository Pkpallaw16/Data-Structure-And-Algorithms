n=int(input("eneter size of array"))
arr=[]
for i in range(n):
    arr.append(int(input()))
mx=max(arr)
for ht in range(mx,0,-1):
    for i in range(len(arr)):
        if arr[i]>=ht:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

