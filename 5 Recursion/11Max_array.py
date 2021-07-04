def max_array(arr,id):
    if id==len(arr)-1:
        return arr[id]
    misa=max_array(arr,id+1)
    if arr[id]>misa:
        return arr[id]
    else:
       return misa

n=int(input("size of array"))
arr=[]
for i in range(n):
    arr.append(int(input()))
print(max_array(arr,0))