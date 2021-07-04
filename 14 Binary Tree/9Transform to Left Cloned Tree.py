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
def Transform_to_Left_Cloned_Tree(root):
    if root==None:
        return None
    node = Node(root.data)
    if root.left != None:
        node.left = root.left
        root.left = node

    else:
        root.left = node
    Transform_to_Left_Cloned_Tree(root.left.left)
    Transform_to_Left_Cloned_Tree(root.right)

def Transform_to_Left_Cloned_Tree_2nd(root):
    if root==None:
        return None

    lcr=Transform_to_Left_Cloned_Tree_2nd(root.left)
    rcr=Transform_to_Left_Cloned_Tree_2nd(root.right)
    nn = Node(root.data,lcr,None)
    root.left=nn
    root.right=rcr
    return root


def fun():
    arr=[50,25,12,None,None,37,None,None,75,62,None,None,87,None,None]
    root=construct(arr)
    display(root)
    #Transform_to_Left_Cloned_Tree(root)
    print()
    #display(root)
    Transform_to_Left_Cloned_Tree_2nd(root)
    print()
    display(root)
fun()