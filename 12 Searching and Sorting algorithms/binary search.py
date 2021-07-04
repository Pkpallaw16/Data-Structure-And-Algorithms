def bSearch(l, lo,hi,data):
    #O(logn)
    if lo>hi:
        return -1
    mid = (lo + hi) // 2
    if l[mid] == data:
        return mid
    elif l[mid] < data:
        return bSearch(l, mid + 1, hi, data)
    else:
        return bSearch(l, lo, mid - 1, data)



l = [10, 20, 30, 40, 50, 60]

print(bSearch(l, 0,len(l)-1,5))

