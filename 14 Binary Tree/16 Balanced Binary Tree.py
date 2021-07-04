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
Isbal=True
def Balanced_Binary_Tree(root):
    global Isbal
    if root==None:
        return -1
    lht=Balanced_Binary_Tree(root.left)
    rht=Balanced_Binary_Tree(root.right)
    dif=abs(lht-rht)
    if dif>1:
        Isbal=False
    return max(lht,rht)+1
def fun():
    arr=[50,25,12,None,None,37,None,None,75,62,None,None,87,None,None]
    root=construct(arr)
    display(root)
    Balanced_Binary_Tree(root)
    print(Isbal)
fun()

