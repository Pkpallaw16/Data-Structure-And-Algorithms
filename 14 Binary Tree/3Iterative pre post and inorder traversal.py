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
def iterativePre_post_inorder_traversal(root):
    st=[]
    root_pair=pair(root,1)
    st.append(root_pair)
    pre=""
    in_order=""
    post=""
    while len(st)>0:
        top=st[-1]
        if top.state==1:
            pre+=str(top.node.data)+" "
            top.state+=1
            if top.node.left!=None:
                new_pair=pair(top.node.left,1)
                st.append(new_pair)
        elif top.state==2:
            in_order+=str(top.node.data)+" "
            top.state += 1
            if top.node.right!=None:
                new_pair=pair(top.node.left,1)
                st.append(new_pair)
        else:
            post+=str(top.node.data)+" "
            st.pop()
    print(pre)
    print(in_order)
    print(post)

def fun():
    arr=[50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]
    root=construct(arr)
    display(root)
    iterativePre_post_inorder_traversal(root)
fun()
