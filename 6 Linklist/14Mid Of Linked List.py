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
    def getNthNode(self,pos):
        temp=self.head
        while pos>0:
            temp=temp.next
            pos-=1
        return temp

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def mid_linknlist(self):
        pos=int(self.size/2)
        if self.size%2==0:
            n1=self.getNthNode(pos-1)
            n2=self.getNthNode(pos)
            print(n1.data,n2.data)
        else:
            n2 = self.getNthNode(pos)
            print(n2.data)
    def mid1(self):
        if self.head==None:
            return -1
        slow=self.head
        fast=self.head.next
        while fast!= None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    def mid2(self):
        if self.head==None:
            return -1
        slow=self.head
        fast=self.head
        while fast!= None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow.data

ll=LinkList()
ll.addFirst(10)
ll.addFirst(20)
ll.addFirst(30)
ll.addFirst(50)
ll.addFirst(51)
ll.addFirst(52)
ll.display()
print(ll.mid1())
print(ll.mid2())

