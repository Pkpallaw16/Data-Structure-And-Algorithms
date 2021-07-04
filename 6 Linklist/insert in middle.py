import math
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def printList(head):
    curr = head
    while curr!= None:
        print(curr.key, end=" ")
        curr = curr.next

def insertInMid(head,node):
    #code here
    if head==None:
        head= node
    elif head.next==None:
        head.next=node
    else:
        cur=head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        print(count)
        pos=math.ceil(count/2)
        print(pos)
        new_cur=head
        i=0
        while i<pos-1:
            new_cur=new_cur.next
            i+=1
        node.next=new_cur.next
        new_cur.next=node
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
node= Node(30)
insertInMid(head,node)
printList(head)


