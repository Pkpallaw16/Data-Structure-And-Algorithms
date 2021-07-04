class MaxHeap:
    def __init__(self,l=[]):
        self.data=l
    def parent(self,index):
        return (index-1)//2
    def lchild(self,parent):
        return 2*parent+1
    def rchild(self,parent):
        return 2 * parent + 2
    def max_downheapify(self,index,heap_len):
        lci=self.lchild(index)
        rci=self.rchild(index)
        largest=index
        if lci<heap_len and self.data[lci]>self.data[largest]:
            largest=lci
        if rci<heap_len and self.data[rci]>self.data[largest]:
            largest=rci
        if largest!=index:
            self.data[largest],self.data[index]=self.data[index],self.data[largest]
            self.max_downheapify(largest,heap_len)

    def heap_sort(self):
        n=len(self.data)-1
        pi=self.parent(n)
        for i in range(pi,-1,-1):
            self.max_downheapify(i,n)
        for i in range(n,-1,-1):
            self.data[0],self.data[i]=self.data[i],self.data[0]
            self.max_downheapify(0,i)
        print(self.data)

heap=MaxHeap([9,3,5,2,6,10,30,4,7,50])
heap.heap_sort()