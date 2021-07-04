import heapq
def K_largest(arr,k):
    hp=[]
    for i in range(len(arr)):
        if i <k:
            heapq.heappush(hp,arr[i])
        else:
            if arr[i]>hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp,arr[i])
    for i in range(len(hp)):
        print(heapq.heappop(hp),end=" ")

arr=[8,30,4,5,6,23,56,90,40,80]
K_largest(arr,4)
