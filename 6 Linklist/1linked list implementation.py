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


    def addLast(self,key):
        if self.size == 0:
            nn = Node(key)
            self.head = nn
            self.tail = nn
            self.size += 1
        else:
            nn = Node(key)
            self.tail.next=nn
            self.tail = nn
            self.size+=1
    def getNthNode(self,pos):
        temp=self.head
        while pos>0:
            temp=temp.next
            pos-=1
        return temp

    def addAt(self,val,indx):
        if indx<0 or indx>self.size:
            print("invalid position")
            return
        elif indx==0:
            self.addFirst(val)
        elif indx==ll.size:
            self.addLast(val)
        else:
            nm1=self.getNthNode(indx-1)
            nn=Node(val)
            nn.next=nm1.next
            nm1.next=nn
            self.size+=1

    def getFirst(self):
        if self.size==0:
            return -1
        return self.head.data

    def getLast(self):
        if self.size==0:
            return -1
        return self.tail.data
    def getAt(self,indx):
        if indx<0 or indx>=self.size:
            return -1
        n=self.getNthNode(indx)
        return n.data

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    def removeFirst(self):
        if ll.size==0:
            return -1
        elif ll.size==1:
            val=ll.head.data
            self.head=None
            self.tail=None
            ll.size -= 1
            return val
        else:
            val = ll.head.data
            ll.head=ll.head.next
            ll.size-=1
            return val
    def removeLast(self):
        if ll.size==0:
            return -1
        elif ll.size==1:
            val=ll.head.data
            self.head=None
            self.tail=None
            ll.size-=1
            return val
        else:
            temp=ll.head
            val=ll.tail.data
            while temp.next!=ll.tail:
                temp=temp.next
            ll.tail=temp
            temp.next=None
            ll.size-=1
            return val
    def removeAt(self,indx):
        if indx<0 or indx>=self.size:
            return -1
        elif indx==0:
            self.removeFirst()
        elif indx==ll.size-1:
            self.removeLast()
        else:
            n=self.getNthNode(indx-1)
            val=n.next.data
            n.next=n.next.next
            ll.size-=1
            return val
    def reverse_Linklis_pointer_iterative(self):
        prev=None
        curr=self.head
        self.tail=self.head
        while curr.next!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        curr.next=prev
        self.head=curr
    def reverse_list_data_iterative(self):
        left=0
        right=self.size-1
        while left<right:
            lnode=self.getNthNode(left)
            rnode=self.getNthNode(right)
            temp=lnode.data
            lnode.data=rnode.data
            rnode.data=temp
            left+=1
            right-=1


ll=LinkList()
ll.addFirst(10)
ll.addLast(20)
ll.addLast(30)
ll.display()
ll.addFirst(5)
ll.display()
#ll.reverse_Linklis()
ll.display()
print(ll.size)
print(ll.getAt(3))
ll.addAt(50,3)
ll.display()
print(ll.removeFirst())
ll.display()
print(ll.removeAt(2))
ll.display()
print(ll.removeLast())
ll.display()

