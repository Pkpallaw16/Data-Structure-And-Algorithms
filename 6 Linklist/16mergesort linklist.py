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
    def getNthNode(self,pos):
        temp=self.head
        while pos>0:
            temp=temp.next
            pos-=1
        return temp
    def get_size(self,head,tail):
        count=1
        temp=head
        while temp!=tail:
            count+=1
            temp=temp.next
    def mid_for_merge_sort(self,head):

        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        #print(head.data, tail.data, end="mid")
        return slow
    def merge_two_list(self,l1,l2):
        first=l1.head
        second=l2.head
        res=LinkList()
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
    def merge_sort_linklist(self,head):
        if head.next==None:
            bll=LinkList()
            bll.addLast(head.data)
            bll.display()
            return bll
        #sz=self.get_size(head,tail)
        #m=int(sz/2)
        mid=self.mid_for_merge_sort(head)
        mid_next=mid.next
        mid.next=None
        first=self.merge_sort_linklist(head)
        second=self.merge_sort_linklist(mid_next)
        res=self.merge_two_list(first,second)
        return res
ll=LinkList()
ll.addLast(10)
ll.addLast(20)
ll.addLast(15)
ll.addLast(50)
ll.addLast(25)
ll.addLast(52)
ll.display()
print(ll.head,ll.tail)
res=ll.merge_sort_linklist(ll.head)
res.display()


