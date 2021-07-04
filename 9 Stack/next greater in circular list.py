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
    st=[]
    while len(stack)>0:
        j=stack.pop()
        st.append(j)
        for i in range(j):
            if arr[j]<arr[i]:
                st.pop()
                res[j]=arr[i]
                break
    while len(st)>0:
        res[st.pop()]=-1


    return res

arr=[2, 5, 9, 3, 1, 12, 6, 8, 7]
print(next_greater_ele(arr))
