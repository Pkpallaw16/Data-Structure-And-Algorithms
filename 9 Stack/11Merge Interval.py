class pair:
    def __init__(self,st,end):
        self.st=st
        self.end=end
    def __lt__(self,other):
        return self.st<other.st

def mergeIntervals(arr):
    # Sorting based on the increasing order
    # of the start intervals
    #arr.sort(key=lambda x: x[0])
    print(arr)
    pairs=[]
    for i in range(len(arr)):
        pairs.append(pair(arr[i][0],arr[i][1]))
    pairs.sort()
    for i in range(len(pairs)):
        print(pairs[i].st,pairs[i].end)
    stack=[]
    stack.append(pairs[0])
    for i in range(1,len(pairs)):
        p=pairs[i]
        if p.st<=stack[-1].end:
            if p.end>stack[-1].end:
                stack[-1].end=p.end
        else:
            stack.append(p)
    for inter in stack:
        print(inter.st,inter.end)

arr= [[22,28],[1,8],[25,27],[14,19],[27,30],[5,12]]
mergeIntervals(arr)
