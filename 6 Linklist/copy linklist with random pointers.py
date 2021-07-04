class Node:
    def __init__(self,val=0,next=None,random=None):
        self.val=val
        self.next=next
        self.random=random
def display(head):
    temp=head
    while temp!=None:
        print("(",temp.val,end="->")
        if temp.random!=None:
            print(temp.random.val,")")
        else:
            print(-1, ")")
        temp=temp.next
def copyRandomlist(head1):
    temp=head1
    dummmy=Node(-1)
    prev=dummmy
    while temp!=None:
        prev.next = Node(temp.val)
        prev = prev.next
        temp=temp.next
    #connecting zigzag
    head2=dummmy.next
    t1=head1
    t2=head2
    while t1!=None and t2!=None:
        n1=t1.next
        n2=t2.next
        t1.next=t2
        t2.next=n1
        t1=n1
        t2=n2
    #set random pointer
    t1=head1
    while t1!=None:
        if t1.random==None:
            t1.next.random=None
        else:
            t1.next.random=t1.random.next
        t1=t1.next.next
    d1=Node(-1)
    d2=Node(-1)
    t1=d1
    t2=d2
    temp=head1
    while temp!=None:
        t1.next=temp
        t2.next=temp.next
        t1=t1.next
        t2=t2.next
        temp=temp.next.next
    t1.next=None
    t2.next=None
    return d2.next


def fun():
    listnode=[]
    prev=None
    n=int(input("enter number of nodes"))
    for i in range(n):
        listnode.append(Node(0))
        if prev!=None:
            prev.next=listnode[i]
        prev=listnode[i]
    for i in range(n):
        val=input("enter value ")
        idx=int(input("enter random index "))
        listnode[i].val=val
        if idx!=-1:
            listnode[i].random=listnode[idx]
    display(listnode[0])
    head=copyRandomlist(listnode[0])
    display(head)



fun()
