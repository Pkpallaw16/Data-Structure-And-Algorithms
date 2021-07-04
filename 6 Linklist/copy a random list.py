class Node:
    def __init__(self, data=0,next=None,random=None):
        self.data = data
        self.next = next
        self.random=random
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

    def copy_random_listt(self,head):
        dummy=Node(-1)
        temp=dummy
        cur=head
        #clone without random
        while cur!=None:
            nn=Node(cur.data)
            temp.next=nn
            temp=nn
            cur=cur.next
        head2=dummy.next
        t1=head
        t2=head2




