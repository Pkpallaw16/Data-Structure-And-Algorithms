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

arr=[1,2,3,4,5,6,7,8]
rotate(arr,-3)
print(arr)