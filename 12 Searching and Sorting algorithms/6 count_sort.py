def count_sort(arr,fre_range):
    n=len(arr)
    freq=[0 for i in range(fre_range)]
    for i in range(n):
        freq[arr[i]]+=1
    k=0
    for i in range(fre_range):
        for j in range(freq[i]):
            arr[k]=i
            k+=1
arr=[1,2,3,3,1,1,1,4,5,6,2,2,6,8,2,5,5,9,1,2,3]
count_sort(arr,10)
print(arr)