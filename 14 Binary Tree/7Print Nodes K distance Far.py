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
        bst.append(root)
        return bst
    lres=Node_to_root_path(root.left,val)
    if len(lres)>0:
        lres.append(root)
        return lres
    rres=Node_to_root_path(root.right,val)
    if len(rres)>0:
        rres.append(root)
        return rres
    return []
def print_nodes(node,k,lis):
    if node==None or node in lis or k<0:
        return
    if k==0:
        print(node.data,end=" ")

    print_nodes(node.left,k-1,lis)
    print_nodes(node.right,k-1,lis)
def print_nodes_k_distance_far(root,val,k):
    l=Node_to_root_path(root,val)
    lis=[]
    for i in range(len(l)):
        print_nodes(l[i],k-i,lis)
        lis.append(l[i])

def PrintKDown(node,blockage,k):
    if node==None or node==blockage or k<0:
        return
    if k==0:
        print(node.data,end=" ")
        return
    PrintKDown(node.left,blockage,k-1)
    PrintKDown(node.right, blockage, k - 1)
def print_Knodes_Far(root,data,k):
    node_to_root=Node_to_root_path(root,data)
    blockage=None
    for n in node_to_root:
        print(n.data,end=" ")
    print()
    for i in range(len(node_to_root)):
        PrintKDown(node_to_root[i],blockage,k-i)
        blockage=node_to_root[i]
def fun():
    arr=[50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]
    root=construct(arr)
    display(root)
    print_nodes_k_distance_far(root,37,2)
    print()
    print_Knodes_Far(root,37,2)
fun()

