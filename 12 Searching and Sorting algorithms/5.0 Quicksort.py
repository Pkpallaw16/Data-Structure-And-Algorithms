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

def quicksort(arr,lo,hi):
    if lo>=hi:
        return
    p = partition_index(arr, lo,hi,arr[hi])
    quicksort(arr, lo, p - 1)
    quicksort(arr, p + 1, hi)

arr=[3,4,1,2,8,9,2,9]
quicksort(arr,0,7)
print(arr)