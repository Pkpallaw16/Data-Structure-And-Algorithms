def all_index_occurance(arr,id,ele,index):
    if id==len(arr):
        return index
    if arr[id]==ele:
        index.append(id)
        all_index_occurance(arr, id + 1, ele,index)
        return index
    else:
        all_index_occurance(arr, id + 1, ele,index)
        return index

def all_index_occ(l,id,ele):
    if len(l)==id:
        return []
    occu=all_index_occ(l,id+1,ele)
    if ele==l[id]:
        occu.append(id)
        return occu
    else:
        return occu

def all_index_occu(arr,data,indx,count):
    if indx==len(arr):
        bres=[0 for i in range(count)]
        return bres
    if arr[indx]==data:
        count+=1
    res=all_index_occu(arr,data,indx+1,count)
    if arr[indx]==data:
        res[count-1]=indx
    return res




n=int(input("size of array"))
arr=[]
for i in range(n):
    arr.append(int(input()))
ele=int(input("enter element"))
index=[]
print(all_index_occurance(arr,0,ele,index))
print(all_index_occu(arr,ele,0,0))