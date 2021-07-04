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
def preorder(root):
    if root != None:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
def postorder1(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
def level_order_traversal(root):
    cur_level=[]
    next_level=[]
    cur_level.append(root)
    while len(cur_level)>0:
        node=cur_level.pop(0)
        print(node.data,end=" ")
        if node.left!=None:
            next_level.append(node.left)
        if node.right!=None:
            next_level.append(node.right)
        if len(cur_level)==0:
            cur_level,next_level=next_level,cur_level
            print()
def level_order_traversal_2nd(root):
    cur_level=[]
    cur_level.append(root)
    cur_level.append("$")
    while len(cur_level)>1:
        if cur_level[0]=="$":
            cur_level.pop(0)
            cur_level.append("$")
            print()
        node=cur_level.pop(0)
        print(node.data,end=" ")
        if node.left!=None:
            cur_level.append(node.left)
        if node.right!=None:
            cur_level.append(node.right)
def level_order_traversal_3nd(root):
    cur_level=[]
    cur_level.append(root)
    while len(cur_level)>0:
        sz=len(cur_level)
        while sz>0:
            node=cur_level.pop(0)
            print(node.data,end=" ")
            if node.left!=None:
                cur_level.append(node.left)
            if node.right!=None:
                cur_level.append(node.right)
            sz-=1
        print()

def fun():
    arr=[50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]
    root=construct(arr)
    display(root)
    preorder(root)
    print()
    postorder(root)
    print()
    postorder1(root)
    print()
    inorder(root)
    print()
    level_order_traversal(root)
    level_order_traversal_2nd(root)
fun()

