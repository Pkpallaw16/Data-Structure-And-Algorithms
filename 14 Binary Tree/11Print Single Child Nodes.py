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
def Print_Single_Child_Nodes(root):
    if root==None:
        return
    elif root.left!=None and root.right==None:
        print(root.data)
    elif root.left==None and root.right!=None:
        print(root.data)
    Print_Single_Child_Nodes(root.left)
    Print_Single_Child_Nodes(root.right)

def Print_Single_Child_Nodes_2nd(node,parent):
    if node==None:
        return
    elif parent!=None and parent.left==node and parent.right==None:
        print(parent.data)
    elif parent!=None and parent.left==None and parent.right==node:
        print(parent.data)
    Print_Single_Child_Nodes(node.left,node)
    Print_Single_Child_Nodes(node.right,node)
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
def fun():
    arr=[50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]
    root=construct(arr)
    display(root)
    Print_Single_Child_Nodes(root)
    print()
    remove_leaf_node_btree(root)

fun()
