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

diamter=0
def diameter_of_binarytree(root):
    global diamter
    maxht = -1
    smaxht = -1
    lh=diameter_of_binarytree(root.left)
    rh=diameter_of_binarytree(root.right)
    if lh>maxht:
        maxht=lh
        smaxht=maxht
    elif lh>smaxht:
        smaxht=lh
    if rh>maxht:
        maxht=rh
        smaxht=maxht
    elif rh>smaxht:
        smaxht=rh
    diamter=max(diamter,(maxht+smaxht+2))
    return maxht+1

