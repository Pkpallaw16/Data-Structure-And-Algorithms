def partition_index(list,lo,hi,pivot):
    i=lo
    j=lo
    while i <=hi:

        if list[i]<=pivot:
            list[i],list[j]=list[j],list[i]
            i+=1
            j+=1
        else:
            i+=1
    return j-1

def quicksort(arr,lo,hi,k):
    if lo>hi:
        return
    p = partition_index(arr, lo,hi,arr[hi])
    if k==p:
        return arr[p]
    elif k<p:
        return quicksort(arr, lo, p - 1,k)
    else:
        return quicksort(arr, p + 1, hi,k)

arr=[3,4,1,2,8,9,2,9]
print(quicksort(arr,0,7,3))
print(arr)