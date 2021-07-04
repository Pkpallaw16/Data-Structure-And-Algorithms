def next_greater_ele(arr):
    stack=[]
    res=[0 for i in range(len(arr))]
    for i in range(len(arr)):
        if not stack:
            stack.append(i)
        else:
            while len(stack)>0 and arr[stack[-1]]<arr[i]:
                res[stack.pop()]=i

            stack.append(i)
    while len(stack)>0:
        res[stack.pop()]=len(arr)
    return res

def sliding_window(arr,k):
    rgi=next_greater_ele(arr)
    j=0
    for i in range(len(arr)-(k-1)):
        if i>j:
            j=i
        while i+k>rgi[j]:
            j=rgi[j]
        print(arr[j])
arr=[2, 9, 3, 8, 1, 7, 12, 6, 14, 4, 32, 0, 7, 19, 8, 12, 6]
sliding_window(arr,4)

