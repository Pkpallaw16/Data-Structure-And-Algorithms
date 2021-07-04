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

    def kth_node_from_end(self,k):
        curr=self.head
        pos=self.head
        size=0
        while curr.next!=None:
            if size<k:
                curr=curr.next
                size+=1
            else:
                pos=pos.next
                curr=curr.next

        return pos.data
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
ll=LinkList()
ll.addFirst(10)
ll.addFirst(20)
ll.addFirst(30)
ll.addFirst(50)
ll.addFirst(51)
ll.addFirst(52)
ll.addFirst(53)
ll.display()
print(ll.kth_node_from_end(3))