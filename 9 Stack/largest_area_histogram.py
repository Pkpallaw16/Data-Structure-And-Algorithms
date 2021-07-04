def next_smaller_ele_left(arr):
    stack=[]
    res=[0 for i in range(len(arr))]
    for i in range(len(arr)-1,-1,-1):
        if not stack:
            stack.append(i)
        else:
            while len(stack)>0 and arr[stack[-1]]>arr[i]:
                res[stack.pop()]=i

            stack.append(i)
    while len(stack)>0:
        res[stack.pop()]=-1
    return res

def next_smaller_ele_right(arr):
    stack=[]
    res=[0 for i in range(len(arr))]
    for i in range(len(arr)):
        if not stack:
            stack.append(i)
        else:
            while len(stack)>0 and arr[stack[-1]]>arr[i]:
                res[stack.pop()]=i

            stack.append(i)
    while len(stack)>0:
        res[stack.pop()]=len(arr)
    return res
def largest_area_histogram(arr):
    lsi=next_smaller_ele_left(arr)

    rsi=next_smaller_ele_right(arr)
    area=0
    for i in range(len(arr)):
        width=rsi[i]-lsi[i]-1
        height=arr[i]
        area=max(area,width*height)
    return area
if __name__=="__main__":
    arr=[6, 2, 5, 4, 5, 1, 6]
    print(largest_area_histogram(arr))



