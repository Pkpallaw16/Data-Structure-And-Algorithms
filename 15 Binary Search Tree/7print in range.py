class Node:
    def __init__(self,val,left=None,right=None):
        self.data=val
        self.left=left
        self.right=right
def construct(data,lo,hi):
    if lo>hi:
        return None
    mid=(lo+hi)//2
    lc=construct(data,lo,mid-1)
    rc=construct(data,mid+1,hi)
    new_node=Node(data[mid],lc,rc)
    return new_node
def display(root):
    if root==None:
        return
    str1=""
    if root.left==None:
        str1+="."
    else:
        str1 += str(root.left.data)
    str1+="<--"+str(root.data)+"--> "
    if root.right==None:
        str1+="."
    else:
        str1 += str(root.right.data)
    print(str1)
    display(root.left)
    display(root.right)
def Print_in_range_bst(root,val1,val2):
    if root==None:
        return
    if root.data<val1 and root.data<val2:
        Print_in_range_bst(root.right, val1, val2)
    elif root.data>val1 and root.data>val2:
        Print_in_range_bst(root.left, val1, val2)
    else:
        Print_in_range_bst(root.right, val1, val2)
        print(root.data,end=" ")
        Print_in_range_bst(root.left, val1, val2)

def fun():
    data=[10,20,30,40,50,60,70,80,90]
    root=construct(data,0,len(data)-1)
    display(root)
    print()
    Print_in_range_bst(root,30,90)
fun()