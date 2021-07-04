def Ceil_and_floor(arr,data):
    lo=0
    hi=len(arr)-1
    ceil=0
    floor=0
    while lo<=hi:
        mid=(lo+hi)//2
        if data<arr[mid]:
            hi=mid-1
            ceil=arr[mid]
        elif data>arr[mid]:
            lo=mid+1
            floor=arr[mid]
        else:
            ceil=arr[mid]
            floor=arr[mid]
            break
    print(ceil)
    print(floor)
Ceil_and_floor([10,20,30,40,50,60,70,80,90],35)