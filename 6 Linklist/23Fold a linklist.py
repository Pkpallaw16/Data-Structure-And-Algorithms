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

    def mid1(self):
        if self.head == None:
            return -1
        slow = self.head
        fast = self.head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse_Linklis_pointer_iterative(self,head):
        prev=None
        curr=head
        while curr.next!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        curr.next=prev
        return curr
    def Fold_linklist(self):
        head1=self.head
        mid=self.mid1()
        head2 = mid.next
        mid.next=None
        head2=self.reverse_Linklis_pointer_iterative(head2)
        t1=head1
        t2=head2
        res=True
        while t1!=None and t2!=None:
            temp1=t1.next
            temp2=t2.next
            t1.next=t2
            t2.next=temp1
            t1=temp1
            t2=temp2
        t1=head1
        while t1.next!=None:
            t1=t1.next
        self.tail=t1



ll=LinkList()
ll.addFirst(1)
ll.addFirst(2)
ll.addFirst(1)
ll.display()
ll.Fold_linklist()
ll.display()
