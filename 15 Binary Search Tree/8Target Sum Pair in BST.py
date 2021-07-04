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
def find_ele_bst(root,val):
    if root==None:
        return False
    if root.data==val:
        return True
    if root.data<val:
        return find_ele_bst(root.right,val)
    if root.data>val:
        return find_ele_bst(root.left,val)
def Target_sum_pair_bst(root,node,tar):
    if node==None:
        return
    Target_sum_pair_bst(root,node.left,tar)
    comp=tar-node.data
    if node.data<comp:
        if find_ele_bst(root,comp):
            print(node.data,comp)
    Target_sum_pair_bst(root, node.right, tar)
def fun():
    data=[10,20,30,40,50,60,70,80,90]
    root=construct(data,0,len(data)-1)
    display(root)
    print()
    Target_sum_pair_bst(root,root,100)
fun()