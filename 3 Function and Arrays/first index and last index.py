def first_last_index(arr,data):
    lo=0
    hi=len(arr)-1
    fi=-1
    li=-1
    while lo<=hi:
        mid=(lo+hi)//2
        if data < arr[mid]:
            hi = mid - 1
        elif data > arr[mid]:
            lo = mid + 1
        else:
            fi = mid
            hi = mid - 1

    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data < arr[mid]:
            hi = mid - 1
        elif data > arr[mid]:
            lo = mid + 1
        else:
            li = mid
            lo = mid + 1

    print(fi,li)

first_last_index([1,3,5,5,5,5,5,6,8,9,10],5)
