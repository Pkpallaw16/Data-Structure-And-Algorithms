class Node:
    def __init__(self, data=0,next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self,head=None,tail=None,size=0):
        self.head=head
        self.tail=tail
        self.size=size

    def addFirst(self,val):
        if self.size==0:
            nn=Node(val)
            self.head=nn
            self.tail=nn
            self.size += 1
        else:
            nn=Node(val)
            nn.next=self.head
            self.size+=1
            self.head=nn

    def display(self):
        h1=self.head
        while h1 != None:
            print(h1.data, end=" ")
            h1=h1.next

    def pairwiseSwap(self):
        # code here
        cur = self.head.next
        prev = self.head
        if self.head.next == None:
            self.display()
            return
        else:
            while cur != None:
                temp = prev.data
                prev.data = cur.data
                cur.data = temp
                prev = prev.next.next
                if cur.next == None:
                    cur = None
                else:
                    cur = cur.next.next
            self.display()

ll=LinkList()
ll.addFirst(10)
ll.addFirst(20)
ll.addFirst(30)
ll.addFirst(5)
ll.display()
ll.pairwiseSwap()
