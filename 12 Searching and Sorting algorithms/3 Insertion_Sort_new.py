def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1

arr=[2,8,3,4,2,5,23,1]
insertionsort(arr)
print(arr)