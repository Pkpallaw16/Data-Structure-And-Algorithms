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
    def removeFirst(self):
        if self.size==0:
            return -1
        elif self.size==1:
            val=self.head.data
            self.head=None
            self.tail=None
            self.size -= 1
            return val
        else:
            val = self.head.data
            self.head=self.head.next
            self.size-=1
            return val

    def k_reverse(self,k):
        prev=LinkList()
        while self.size>0:
            cur = LinkList()
            if self.size>k:
                for i in range(k):
                    data=self.removeFirst()
                    cur.addFirst(data)
            else:
                while self.size>0:
                    data = self.removeFirst()
                    cur.addLast(data)

            if prev.head==None:
                prev=cur
            else:
                prev.tail.next = cur.head
                prev.tail = cur.tail
                prev.size += cur.size
        self.head=prev.head
        self.tail=prev.tail
        self.size=prev.size
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def display_reverse_rcursive(self,cur):
        if cur==None:
            return
        self.display_reverse_rcursive(cur.next)
        print(cur.data,end="  ")
    def reverse_recursive(self,cur,prev):
        if cur.next==None:
            self.head=cur
            cur.next=prev
            return
        temp=cur.next
        cur.next=prev
        prev=cur
        cur=temp
        self.reverse_recursive(cur,prev)
    def reverse_recursive_2nd(self):
        temp=self.head
        self.reversePRhelper(temp)
        temp.next=None
        self.tail=temp
    def reversePRhelper(self,node):
        if node.next==None:
            self.head=node
            return
        self.reversePRhelper(node.next)
        node.next.next=node






ll=LinkList()
ll.addFirst(10)
ll.addLast(20)
ll.addLast(30)
ll.addFirst(12)
ll.addLast(22)
ll.addLast(34)
ll.addFirst(120)
ll.addLast(201)
ll.addLast(301)
ll.addFirst(5)
ll.addFirst(51)
ll.display()
ll.k_reverse(3)
ll.display()
ll.display_reverse_rcursive(ll.head)
print()
ll.display()

ll.reverse_recursive(ll.head,None)
ll.display()
ll.reverse_recursive_2nd()
ll.display()