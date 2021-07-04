import heapq
def Sort_K_sorted_list(arr,k):
    hp=[]
    heapq.heapify(hp)
    j=0
    for i in range(k+1):
        heapq.heappush(hp, arr[i])
    for i in range(k+1,len(arr)):
        if i==len(arr)-1:
            arr[j] = heapq.heappop(hp)
            heapq.heappush(hp, arr[i])
            j += 1
            while len(hp)!=0:
                arr[j]=heapq.heappop(hp)
                j+=1
        else:
            arr[j]=heapq.heappop(hp)
            heapq.heappush(hp,arr[i])
            j+=1
    print(arr)
arr=[3,2,4,1,6,5,7,9,8]
Sort_K_sorted_list(arr,3)


