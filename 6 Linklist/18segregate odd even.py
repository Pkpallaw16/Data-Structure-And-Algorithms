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
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    def remove_duplicate(self):
        temp=self.head
        itr= temp.next
        while itr!=None:
            if temp.data== itr.data:
                itr=itr.next
            else:
                temp.next=itr
                temp=temp.next
                itr=itr.next
        temp.next=itr
    def segregate_odd_even(self):
        unsorted=self.head
        first_even=self.head
        while unsorted!=None:
            if unsorted.data%2==0:
                unsorted=unsorted.next
            else:
                unsorted.data,first_even.data=first_even.data,unsorted.data
                unsorted=unsorted.next
                first_even=first_even.next
    def oddEven(self):
        ehead=Node(-1)
        temp1=ehead
        ohead=Node(-1)
        temp2=ohead
        itr=self.head
        while itr!=None:
            if itr.data%2==0:
                temp1.next=itr
                temp1=temp1.next
            else:
                temp2.next=itr
                temp2=temp2.next
            itr=itr.next

        temp2.next=ehead.next
        temp1.next=None
        self.head=ehead.next
        self.tail=temp1




ll=LinkList()
ll.addFirst(1)
ll.addFirst(2)
ll.addFirst(3)
ll.addFirst(5)
ll.addFirst(5)
ll.addFirst(5)
ll.addFirst(4)
ll.addFirst(1)
ll.addFirst(2)
ll.addFirst(5)
ll.addFirst(6)
ll.addFirst(8)
ll.display()
ll.remove_duplicate()
ll.display()
ll.oddEven()
ll.display()