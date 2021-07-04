import heapq
class Fpair:
    def __init__(self,val,wt):
        self.val=val
        self.wt=wt
        self.frac=round(float(val/wt),2)
    def __lt__(self, other):
        return self.frac>other.frac
def printFractionalKnapsack(wts,vals,cap):
    hp=[]
    for i in range(len(wts)):
        heapq.heappush(hp,Fpair(vals[i],wts[i]))
    profit=0
    while len(hp)>0 and cap>0:
        rem=heapq.heappop(hp)
        if rem.wt<=cap:
            profit+=rem.val
            cap-=rem.wt
        else:
            profit+=rem.frac*cap
            cap=0
    print(profit)
vals=[33,14,50,9,8,11,6,40,2,15]
wts=[7,2,5,9,3,2,1,10,3,3]
printFractionalKnapsack(wts,vals,5)