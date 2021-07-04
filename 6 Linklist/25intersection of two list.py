def findIntersection(one,two):
    head1=one.head
    head2=two.head
    s1=one.size()
    s2=two.size()
    if s1>s2:
        diff=s1-s2
        for i in range(diff):
            head1=head1.next
    else:
        diff=s2-s1
        for i in range(diff):
            head2=head2.next
    while head1!=None and head2!=None and head1!=head2:
        head1=head1.next
        head2=head1.next
    if head1==None or head2==None:
        return None
    else:
        return head1