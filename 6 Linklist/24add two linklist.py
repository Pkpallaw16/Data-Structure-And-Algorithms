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

    def add_two_list(self,one,two):
        one.reverse_Linklis_pointer_iterative()
        two.reverse_Linklis_pointer_iterative()
        one.display()
        two.display()
        p1=one.head
        p2=two.head
        carry=0
        while p1!=None or p2 !=None or carry!=0:
            if p1==None:
                val1=0
            else:
                val1=p1.data
                p1=p1.next
            if p2==None:
                val2=0
            else:
                val2=p2.data
                p2=p2.next
            sum=val1+val2+carry
            val=sum%10
            carry=int(sum/10)
            self.addFirst(val)
        one.reverse_Linklis_pointer_iterative()
        two.reverse_Linklis_pointer_iterative()

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    def AdditionHelper(self,one,i1,two,i2,res):
        if one==None and two==None:
            return 0
        d1=one.data
        d2=two.data
        if i1>i2:
            carry=self.AdditionHelper(one.next,i1-1,two,i2,res)
            sum1=d1+carry

        elif i1<i2:
            carry = self.AdditionHelper(one, i1, two.next, i2-1,res)
            sum1=d2+carry

        else:
            carry = self.AdditionHelper(one.next, i1-1, two.next, i2 - 1, res)
            sum1 = d1+d2 + carry

        val = sum1 % 10
        ncarry = int(sum1 / 10)
        res.addFirst(val)
        return ncarry



    def sum_linklist_recursive(self,one,two):
        res=LinkList()
        carry=self.AdditionHelper(one.head,one.size,two.head,two.size,res)
        if carry>0:
            res.addFirst(carry)
        return res


one=LinkList()
one.addFirst(1)
one.addFirst(2)
one.addFirst(3)
one.addFirst(5)
one.addFirst(9)
one.addFirst(8)
one.display()
two=LinkList()
two.addFirst(7)
two.addFirst(5)
two.addFirst(4)
two.addFirst(3)
two.display()
ll=LinkList()
ll.add_two_list(one,two)
ll.display()
one.display()
two.display()
res=ll.sum_linklist_recursive(one,two)
res.display()