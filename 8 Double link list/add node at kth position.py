def addNode(head, p, data):
    # Code here
    temp = head
    while p!=0:
        temp=temp.next
        p-=1
    n = Node(data)
    if temp.next is not None:
        n.next = temp.next
        temp.next.prev = n
        n.prev = temp
        temp.next = n
    else:
        n.prev = temp
        temp.next=  n