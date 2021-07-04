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
    if lo>hi:
        return
    partition_index(arr, lo,hi,arr[hi])
    print(arr[0])

def pivotInsortedrotated(l,lo,hi):
    #O(logn)

    if lo==hi:
        return lo
    mid = (lo + hi) // 2
    print(lo,hi,mid)

    if l[mid]< l[hi]:
        #left side including mid
        res=pivotInsortedrotated(l,lo,mid)
    else:
        res= pivotInsortedrotated(l,mid+1,hi)
    return res

def pivotInsortedrotated_2nd(l):
    #O(logn)
    lo=0
    hi=len(l)-1
    while lo<hi:
        mid=(lo+hi)//2
        print(lo, hi, mid)
        if l[mid]<l[hi]:
            hi=mid
        else:
            lo=mid+1
    return l[lo]
arr=[15,16,19,21,23,24,1,2,12]
print(arr[pivotInsortedrotated(arr,0,8)])
#quicksort(arr,0,8)
print(pivotInsortedrotated_2nd(arr))

