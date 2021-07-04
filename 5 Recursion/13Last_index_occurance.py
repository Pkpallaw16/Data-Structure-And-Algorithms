def last_index_occurance(arr,id,ele):
    if id==-1:
        return -1
    if arr[id]==ele:
        return id
    else:
        lio = last_index_occurance(arr, id -1, ele)
        return lio

def last_index_occ(arr,indx,dtf):
    if indx==len(arr):
        return -1
    last_index=last_index_occ(arr,indx+1,dtf)
    if last_index==-1 and arr[indx]==dtf:
        last_index=indx
    return last_index

n=int(input("size of array"))
arr=[]
for i in range(n):
    arr.append(int(input()))
ele=int(input("enter element"))
print(last_index_occurance(arr,n-1,ele))
print(last_index_occ(arr,0,ele))