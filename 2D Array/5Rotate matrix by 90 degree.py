def Rotate_matrix_by_90_degree(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr[i])):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    for i in range(len(arr)):
        li=0
        ri=len(arr[i])-1
        while li<ri:
            arr[i][li],arr[i][ri]=arr[i][ri],arr[i][li]
            li+=1
            ri-=1

    print(arr)


n1=int(input("eneter size of array"))
n2=int(input("eneter size of array"))
arr1=[[int(input()) for i in range(n2)] for j in range(n1)]
print(arr1)
Rotate_matrix_by_90_degree(arr1)


