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
def size(root):
    if root == None:
        return 0
    else:
        ls = size(root.left)
        rs = size(root.right)
    return ls + rs + 1

def size1(root):
    sz=0
    if root == None:
        return 0
    else:
        sz+= size(root.left)
        sz+= size(root.right)
    return sz + 1
def sum(root):
    if root == None:
        return 0
    else:
        lsum = sum(root.left)
        rsum = sum(root.right)
    return lsum + rsum + root.data
def max_tree(root):
    if root == None:
        return -sys.maxsize
    else:
        lmax = max_tree(root.left)
        rmax = max_tree(root.right)
    return max(lmax,rmax,root.data)
def height(root):
    if root == None:
        return -1
    else:
        lh = height(root.left)
        rh = height(root.right)
    return max(lh,rh)+1
def fun():
    arr=[50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]
    root=construct(arr)
    display(root)
    print(size(root))
    print(size1(root))
    print(sum(root))
    print(max_tree(root))
    print(height(root))
fun()
