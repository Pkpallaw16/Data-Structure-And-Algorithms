def count_sort(arr,lo,hi):
    n=len(arr)
    fre_range=hi-lo+1
    freq=[0 for i in range(fre_range)]
    for i in range(n):
        val=arr[i]
        index=val-lo
        freq[index]+=1
    print(freq)
    k=0
    for i in range(fre_range):
        for j in range(freq[i]):
            arr[k]=i+lo
            k+=1
arr=[1,2,3,3,1,-1,-2,-1,1,1,4,5,0,0,-1,-1,-2,6,2,2,6,8,2,5,5,9,1,2,3]
count_sort(arr,-2,9)
print(arr)