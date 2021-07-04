def merge(arr1,arr2):
    arr3=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    if len(arr1)>len(arr2):
        while i <len(arr1):
            arr3.append(arr1[i])
            i+=1
    else:
        while j <len(arr2):
            arr3.append(arr2[j])
            j+=1
    return arr3
def mergesort(arr,lo,hi):
    if lo==hi:
        bres=[]
        bres.append(arr[lo])
        return bres
    mid=(lo+hi)//2
    arr1=mergesort(arr,lo,mid)
    arr2=mergesort(arr,mid+1,hi)
    res=merge(arr1,arr2)
    return res
print(mergesort([1,5,4,6,3,2,4,6,8],0,8))