def stock_span(arr):
    stack=[]
    res=[0 for i in range(len(arr))]
    for i in range(len(arr)-1,-1,-1):
        if not stack:
            stack.append(i)
        else:
            while len(stack)>0 and arr[stack[-1]]<arr[i]:
                indx=stack.pop()
                res[indx]=indx-i

            stack.append(i)
    while len(stack)>0:
        indx=stack.pop()
        res[indx]=indx+1
    return res

arr=[2, 5, 9, 3, 1, 12, 6, 8, 7]
print(stock_span(arr))
