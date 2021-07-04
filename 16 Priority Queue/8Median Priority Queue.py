import heapq
class Median_Priority_Queue:
    def __init__(self):
        self.lq=[]
        self.rq=[]
    def add(self, val):
        if len(self.rq)>0 and self.rq[0]<val:
            heapq.heappush(self.rq,val)
        else:
            heapq.heappush(self.lq,-1*val)
        if len(self.lq)-len(self.rq)>1:
            heapq.heappush(self.rq,-1*heapq.heappop(self.lq))
        elif len(self.rq)-len(self.lq)>1:
            heapq.heappush(self.lq,-1*heapq.heappop(self.rq))
        print(self.lq,self.rq)
    def remove(self):
        if self.size()==0:
            print("underflow")
            return -1
        if len(self.lq)>=len(self.rq):
            val=-1*heapq.heappop(self.lq)
        else:
            val=heapq.heappop(self.rq)

        print(self.lq, self.rq)
        return val
    def peek(self):
        if self.size()==0:
            print("underflow")
            return -1
        if len(self.lq)>=len(self.rq):
            val=-1*self.lq[0]
        else:
            val=self.rq[0]
        return val
    def size(self):
        return len(self.lq)+len(self.rq)
mpq=Median_Priority_Queue()
mpq.add(10)
mpq.add(40)
mpq.add(60)
mpq.add(8)
mpq.add(50)
mpq.add(90)
mpq.add(-5)
mpq.remove()
mpq.remove()
mpq.remove()
mpq.remove()
mpq.remove()
mpq.remove()

