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
def Node_to_root_path(root,val):
    if root==None:
        return []
    if root.data==val:
        bst=[]
        bst.append(root.data)
        return bst
    lres=Node_to_root_path(root.left,val)
    if len(lres)>0:
        lres.append(root.data)
        return lres
    rres=Node_to_root_path(root.right,val)
    if len(rres)>0:
        rres.append(root.data)
        return rres
    return []
def find(root,val):
    if root==None:
        return False
    if root.data==val:
        return True
    lc=find(root.left,val)
    if lc:
        return True
    rc=find(root.right,val)
    if rc:
        return True
    return False
path=[]
def Node_to_root_path_2nd(root,val):
    global path
    if root == None:
        return False
    if root.data == val:
        path.append(root.data)
        return True
    lc = Node_to_root_path_2nd(root.left,val)
    if lc:
        path.append(root.data)
        return True
    rc = Node_to_root_path_2nd(root.right, val)
    if rc:
        path.append(root.data)
        return True
    return False

def fun():
    arr=[50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]
    root=construct(arr)
    display(root)
    print(find(root, 75))
    print(Node_to_root_path(root,37))
    Node_to_root_path_2nd(root, 37)
    print(path)
fun()
