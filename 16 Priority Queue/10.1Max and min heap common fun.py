class myMinHeap:
    def __init__(self,flag=False):
        self.data = []  # list to store values of heap items
        self.flag=flag
    def parent(self, i):
        return (i - 1) // 2

    def lChild(self, i):
        return 2 * i + 1

    def rChild(self, i):
        return 2 * i + 2

    def insert(self, x):
        self.data.append(x)
        self.upheapify(len(self.data)-1)
    def remove(self):
        if len(self.data)==0:
            print("underflow")
            return
        self.data[0],self.data[len(self.data)-1]=self.data[len(self.data)-1],self.data[0]
        val=self.data.pop()
        self.downheapify(0)
        return val
    def checkpriority(self,ci,pi):
        if self.flag==True:
            if self.data[ci]>self.data[pi]:
                return 1
        else:
            if self.data[ci]<self.data[pi]:
                return 1
        return 0
    def downheapify(self,index):
        li=self.lChild(index)
        ri=self.rChild(index)
        smallest=index
        if li < len(self.data) and self.checkpriority(li,smallest)>0:
            smallest = li
        if ri < len(self.data) and self.checkpriority(ri,smallest)>0:
            smallest = ri

        if smallest != index:
            self.data[smallest], self.data[index] = self.data[index], self.data[smallest]
            self.downheapify(smallest)

    def upheapify(self,index):
        if index==0:
            return
        pi=self.parent(index)
        if self.checkpriority(index,pi)>0:
            self.data[pi],self.data[index]=self.data[index],self.data[pi]
            self.upheapify(pi)
    def size(self):
        return len(self.data)
    def displap(self):
        print(self.data)
    def peek(self):
        if len(self.data)==0:
            print("underflow")
            return -1
        return self.data[0]

minHeap = myMinHeap(True)
minHeap.insert(5)
minHeap.insert(3)
minHeap.insert(17)
minHeap.insert(10)
minHeap.insert(84)
minHeap.insert(19)
minHeap.insert(6)
minHeap.insert(22)
minHeap.insert(9)
minHeap.displap()
print(minHeap.remove())
minHeap.displap()
while minHeap.size()>0:
    print(minHeap.remove())

