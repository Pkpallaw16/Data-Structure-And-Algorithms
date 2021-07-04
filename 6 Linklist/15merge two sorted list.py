class Node:
    def __init__(self, data=0,next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self,head=None,tail=None,size=0):
        self.head=head
        self.tail=tail
        self.size=size

    def addLast(self, key):
        if self.size == 0:
            nn = Node(key)
            self.head = nn
            self.tail = nn
            self.size += 1
        else:
            nn = Node(key)
            self.tail.next = nn
            self.tail = nn
            self.size += 1

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def merge_two_list(self,other,res):
        first=self.head
        second=other.head
        while first!=None and second!=None:
            if first.data < second.data:
                res.addLast(first.data)
                first=first.next
            else:
                res.addLast(second.data)
                second=second.next


        while second!=None:
            res.addLast(second.data)
            second=second.next

        while first!=None:
            res.addLast(first.data)
            first=first.next
        return res
    def merge_two_list_2nd(self,other,res):
        first=self.head
        second=other.head
        dummy=Node(-1)
        temp=dummy
        while first!=None and second!=None:
            if first.data < second.data:
                temp.next=first
                temp=temp.next
                first=first.next
            else:
                temp.next=second
                temp=temp.next
                second=second.next
        if first==None:
            temp.next=second
        else:
            temp.next=first
        res.head=dummy.next
        return res


ll=LinkList()
ll.addLast(10)
ll.addLast(20)
ll.addLast(30)
ll.addLast(50)
ll.addLast(51)
ll.addLast(52)
ll.display()
l2=LinkList()
res=LinkList()
l2.addLast(5)
l2.addLast(25)
l2.addLast(40)
l2.addLast(55)
l2.addLast(60)
l2.addLast(70)
l2.addLast(80)
l2.addLast(90)
l2.display()
r1=ll.merge_two_list(l2,res)
r1.display()
res1=LinkList()
r2=ll.merge_two_list_2nd(l2,res1)
r2.display()


