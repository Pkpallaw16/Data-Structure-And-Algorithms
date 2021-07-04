import heapq
class pair:
    def __init__(self,li,di,val):
        self.li=li
        self.di=di
        self.val=val
    def __lt__(self, other):
        return self.val < other.val
def mergeKSortedLists(lists):
    mergedList=[]
    hp=[]
    for i in range(len(lists)):
        pr=pair(i,0,lists[i][0])
        heapq.heappush(hp,pr)
    while len(hp)>0:
        p=heapq.heappop(hp)
        mergedList.append(p.val)
        p.di+=1
        if p.di<len(lists[p.li]):
            p.val=lists[p.li][p.di]
            heapq.heappush(hp,p)
    return mergedList

k=int(input("enter number of list"))
lists=[]
for i in range(k):
    lis=[]
    n=int(input("Number of element"))
    row=input().split()
    for j in range(n):
        lis.append(int(row[j]))
    lists.append(lis)
print(mergeKSortedLists(lists))