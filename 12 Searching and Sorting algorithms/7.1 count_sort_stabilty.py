def count_sort(arr,lo,hi):
    n=len(arr)
    fre_range=hi-lo+1
    freq=[0 for i in range(fre_range)]
    for i in range(n):
        val=arr[i]
        index=val-lo
        freq[index]+=1
    print(freq)
    freq[0]-=1
    for i in range(1,len(freq)):
        freq[i]+=freq[i-1]
    #make a new array fill in reverse direction
    narr= [0 for i in range(n)]
    k=0
    for i in range(len(arr)-1,-1,-1):
        #val to place
        val=arr[i]
        #index in freq
        indx=val-lo
        #position where we have to place in new array
        pos=freq[indx]
        #place it
        narr[pos]=val
        #reduce the prefix sum,i.e position for same upcoming element
        freq[indx]-=1
    for i in range(len(arr)):
        arr[i]=narr[i]
arr=[1,2,3,3,1,-1,-2,-1,1,1,4,5,0,0,-1,-1,-2,6,2,2,6,8,2,5,5,9,1,2,3]
count_sort(arr,-2,9)
print(arr)