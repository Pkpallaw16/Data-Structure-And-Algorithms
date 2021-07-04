def print_array(arr,id):
    if id==len(arr):
        return
    print(arr[id])
    print_array(arr,id+1)
    print(arr[id])

n=int(input("size of array"))
arr=[]
for i in range(n):
    arr.append(int(input()))
print_array(arr,0)
