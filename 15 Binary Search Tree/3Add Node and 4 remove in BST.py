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
def add_node_bst(root,val):
    if root==None:
        return Node(val)
    if root.data>val:
        root.left=add_node_bst(root.left,val)
    else:
        root.right=add_node_bst(root.right,val)
    return root
def remove_node_bst(root,val):
    if root==None:
        return
    if root.data==val:
        if root.left==None and root.right==None:
            return None
        elif root.left==None and root.right!=None:
            return root.left
        elif root.left!=None and root.right==None:
            return root.right
        else:
            node=root.left
            while node.right!=None:
                node=node.right
            root.data=node.data
            root.left=remove_node_bst(root.left,node.data)
            return root
    if root.data>val:
        root.left=remove_node_bst(root.left,val)
    elif root.data<val:
        root.right=remove_node_bst(root.right,val)
    return root
def remove_node_bst_2nd(root,val):
    if root==None:
        return
    if root.data>val:
        root.left=remove_node_bst_2nd(root.left,val)
    elif root.data<val:
        root.right=remove_node_bst_2nd(root.right,val)
    else:
        if root.left!=None and root.right!=None:
            node = root.left
            while node.right != None:
                node = node.right
            root.data = node.data
            root.left=remove_node_bst(root.left, node.data)
            return root
        elif root.left!=None:
            return root.left
        elif root.right!=None:
            return root.right
        else:
            return None
    return root
def fun():
    data=[10,20,30,40,50,60,70,80,90]
    root=construct(data,0,len(data)-1)
    display(root)
    add_node_bst(root,100)
    print()
    display(root)
    remove_node_bst(root,70)
    print()
    display(root)
    remove_node_bst(root, 70)
    print()
    display(root)


fun()