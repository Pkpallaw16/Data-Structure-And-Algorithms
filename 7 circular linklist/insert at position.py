class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtPosition(head,pos,data):
    #code here
    temp=Node(data)
    cur=head
    c=1
    while c<pos:
        cur=cur.next
        c+=1
        if cur==head:
            return
    temp.next=cur.next
    cur.next=temp

def printCircular(head):
    if head == None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(21)
head.next.next.next = Node(22)
head.next.next.next.next = Node(24)
head.next.next.next.next.next = head
insertAtPosition(head,4,23)
printCircular(head)

