def first_index_occurance(arr,id,ele):
    if id==len(arr):
        return -1
    if arr[id]==ele:
        return id
    else:
        fio = first_index_occurance(arr, id + 1, ele)
        return fio

n=int(input("size of array"))
arr=[]
for i in range(n):
    arr.append(int(input()))
ele=int(input("enter element"))
print(first_index_occurance(arr,0,ele))