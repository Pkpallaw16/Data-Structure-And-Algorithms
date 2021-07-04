def getLength(head):
    if not head:
        return 0

    c=1
    t=head
    while t.next!=head:
        t=t.next
        c+=1
    return c
