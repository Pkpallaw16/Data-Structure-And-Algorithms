import sys
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
def size_bst(root):
    if root==None:
        return 0
    lsz=size_bst(root.left)
    rsz=size_bst(root.right)
    return lsz+rsz+1
def sum_bst(root):
    if root==None:
        return 0
    lsz=sum_bst(root.left)
    rsz=sum_bst(root.right)
    return lsz+rsz+root.data
def max_bst(root):
    if root==None:
        return -sys.maxsize
    lmax=max_bst(root.left)
    rmax=max_bst(root.right)
    return max(lmax,rmax,root.data)
def max_bst_2nd(root):
    if root.right!=None:
        return max_bst_2nd(root.right)
    else:
        return root.data
def min_bst(root):
    if root==None:
        return sys.maxsize
    lmax=min_bst(root.left)
    rmax=min_bst(root.right)
    return min(lmax,rmax,root.data)
def min_bst_2nd(root):
    if root.left!=None:
        return min_bst_2nd(root.left)
    else:
        return root.data
def find_ele_bst(root,val):
    if root==None:
        return False
    if root.data==val:
        return True
    if root.data<val:
        return find_ele_bst(root.right,val)
    if root.data>val:
        return find_ele_bst(root.left,val)
def fun():
    data=[10,20,30,40,50,60,70,80,90]
    root=construct(data,0,len(data)-1)
    display(root)
    print(size_bst(root))
    print(sum_bst(root))
    print(max_bst(root))
    print(max_bst_2nd(root))
    print(min_bst(root))
    print(min_bst_2nd(root))
    print(find_ele_bst(root,60))
fun()