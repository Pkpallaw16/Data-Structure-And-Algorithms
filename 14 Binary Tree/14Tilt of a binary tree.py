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
tilt=0
def tilt_of_binary_tree(root):
    global tilt
    if root ==None:
        return 0
    lsum=tilt_of_binary_tree(root.left)
    rsum=tilt_of_binary_tree(root.right)

    local_tilt=abs(lsum-rsum)
    tilt+=local_tilt
    total_sum=lsum+rsum+root.data
    return total_sum
def fun():
    arr=[50,25,12,None,None,37,None,None,75,62,None,None,87,None,None]
    root=construct(arr)
    display(root)
    tilt_of_binary_tree(root)
    print(tilt)
fun()