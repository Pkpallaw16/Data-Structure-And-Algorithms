def Diagonal_Traversal(arr):
    for g in range(len(arr)):
        i=0
        for j in range(g,len(arr)):
            print(arr[i][j])

n1=int(input("eneter size of array"))
n2=int(input("eneter size of array"))
arr1=[[int(input()) for i in range(n2)] for j in range(n1)]
print(arr1)
Diagonal_Traversal(arr1)