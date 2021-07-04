def Spiral_Traversal_martix(arr):
    r_begin=0
    r_end=len(arr)-1
    c_begin=0
    c_end=len(arr[0])-1
    total_count=len(arr)*len(arr[0])
    count=0
    while count<total_count:
        if count<total_count:
            for i in range(r_begin,r_end+1):
                print(arr[i][c_begin])
                count+=1
            c_begin+=1
        if count < total_count:
            for i in range(c_begin,c_end+1):
                print(arr[r_end][i])
                count += 1
            r_end-=1
        if count<total_count:
            for i in range(r_end,r_begin-1,-1):
                print(arr[i][c_end])
                count += 1
            c_end-=1
        if count<total_count:
            for i in range(c_end,c_begin-1,-1):
                print(arr[r_begin][i])
                count += 1
            r_begin+=1

n1=int(input("eneter size of array"))
n2=int(input("eneter size of array"))
arr1=[[int(input()) for i in range(n2)] for j in range(n1)]
print(arr1)
Spiral_Traversal_martix(arr1)