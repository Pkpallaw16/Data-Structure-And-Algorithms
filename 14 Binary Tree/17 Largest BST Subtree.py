import sys
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
class BSTpair:
    def __init__(self,isbst=True,min=sys.maxsize,max=-sys.maxsize):
        self.isBSt=isbst
        self.min=min
        self.max=max
        self.size=0
        self.data=None

def Largest_BST_Subtree(root):
    if root==None:
        bp=BSTpair()
        return bp
    lp=Largest_BST_Subtree(root.left)
    rp=Largest_BST_Subtree(root.right)
    new_pair=BSTpair()
    new_pair.isBSt=lp.isBSt and rp.isBSt and (root.data>=lp.max and root.data<=rp.min)
    new_pair.min=min(root.data,lp.min,rp.min)
    new_pair.max=max(root.data,lp.max,rp.max)
    if new_pair.isBSt:
        new_pair.size=lp.size+rp.size+1
        new_pair.data=root.data
    else:
        if lp.size>rp.size:
            new_pair.size=lp.size
            new_pair.data=lp.data
        else:
            new_pair.size = rp.size
            new_pair.data = rp.data

    return new_pair

def fun():
    arr=[50,25,12,None,None,37,None,None,75,62,None,None,87,None,None]
    root=construct(arr)
    display(root)
    bp=Largest_BST_Subtree(root)
    print(bp.data,bp.size)

fun()

