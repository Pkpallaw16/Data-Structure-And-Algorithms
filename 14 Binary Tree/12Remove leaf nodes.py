class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class pair:
    def __init__(self,node,state):
        self.node=node
        self.state=state
def construct(arr):
    root=Node(arr[0])
    stack=[]
    stack.append(pair(root,0))
    indx=0
    while len(stack)>0:
        p=stack[-1]
        if p.state==0:
            indx+=1
            if arr[indx]!=None:
                nn=Node(arr[indx])
                p.node.left=nn
                stack.append(pair(nn,0))
            p.state+=1
        elif p.state==1:
            indx+=1
            if arr[indx]!=None:
                nn=Node(arr[indx])
                p.node.right=nn
                stack.append(pair(nn,0))
            p.state+=1
        else:
            stack.pop()
    return root

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

def remove_leaf_node_btree(root):
    if root==None:
        return
    lchild=root.left
    rchild=root.right
    if lchild!=None and lchild.left==None and lchild.right==None:
        print(lchild.data)
        root.left=None
    if rchild!=None and rchild.left==None and rchild.right==None:
        print(rchild.data)
        root.right=None
    remove_leaf_node_btree(root.left)
    remove_leaf_node_btree(root.right)

def remove_leaf_node_btree_2nd(root):
    if root==None:
        return
    if root.left==None and root.right==None:
        print(root.data)
        return None
    root.left=remove_leaf_node_btree_2nd(root.left)
    root.right=remove_leaf_node_btree_2nd(root.right)
    return root
def fun():
    arr=[50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]
    root=construct(arr)
    display(root)
    remove_leaf_node_btree_2nd(root)
    print()
    display(root)
    remove_leaf_node_btree(root)

fun()
