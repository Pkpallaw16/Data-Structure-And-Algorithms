def next_greater_ele(arr):
    stack=[]
    res=[0 for i in range(len(arr))]
    for i in range(len(arr)):
        if not stack:
            stack.append(i)
        else:
            while len(stack)>0 and arr[stack[-1]]<arr[i]:
                res[stack.pop()]=arr[i]

            stack.append(i)
    while len(stack)>0:
        res[stack.pop()]=-1
    return res

arr=[2, 5, 9, 3, 1, 12, 6, 8, 7]
print(next_greater_ele(arr))
