import random
def countsort_for_ardix(arr,exp):
    n=len(arr)
    freq = [0 for i in range(10)]
    for i in range(n):
        index = int(arr[i]/exp)%10
        freq[index] += 1
    freq[0] -= 1
    for i in range(1, len(freq)):
        freq[i] += freq[i - 1]
    # make a new array fill in reverse direction
    narr = [0 for i in range(n)]
    for i in range(len(arr) - 1, -1, -1):
        # val to place
        val = int(arr[i]/exp)%10
        # index in freq
        indx = val
        # position where we have to place in new array
        pos = freq[indx]
        # place it
        narr[pos] = arr[i]
        # reduce the prefix sum,i.e position for same upcoming element
        freq[indx] -= 1
    for i in range(len(arr)):
        arr[i] = narr[i]
    print("after sorting on",exp,"place-.")
    print(arr)
def radix_sort(arr):
    #find maximum element
    max1=max(arr)
    exp=1
    while exp<max1:
        countsort_for_ardix(arr,exp)
        exp*=10
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)
arr=[]
n=int(input("enter size of list"))
for i in range(n):
    arr.append(random_with_N_digits(5))
print(arr)
radix_sort(arr)