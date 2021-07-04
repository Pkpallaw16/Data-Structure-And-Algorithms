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

def pathToLeafFromRoot(node,path,sum,lo,hi):
    if node.left==None and node.right==None:
        sum+=node.data
        if sum>lo and sum<hi:
            print(path)
            return
        else:
            return
    pathToLeafFromRoot(node.left,path+[node.data],sum+node.data,lo,hi)
    pathToLeafFromRoot(node.right, path + [node.data],sum+node.data, lo,hi)
def pathToLeafFromRoot_2nd(node,sum,lo,hi):
    if node.left==None and node.right==None:
        sum+=node.data
        if sum>lo and sum<hi:
            bres=[]
            bres.append(node.data)
            return bres
        else:
            return []
    lres=pathToLeafFromRoot_2nd(node.left,sum+node.data,lo,hi)
    if len(lres)>0:
        lres.append(node.data)
        return lres
    rres=pathToLeafFromRoot_2nd(node.right,sum+node.data, lo,hi)
    if len(rres)>0:
        rres.append(node.data)
        return rres
    return []
def fun():
    arr=[50,25,12,None,None,37,30,None,None,40,None,None,75,62,60,None,None,70,None,None,87,None,None]
    root=construct(arr)
    display(root)
    pathToLeafFromRoot(root,[],0,150,250)
    print(pathToLeafFromRoot_2nd(root,0,150,250))
fun()