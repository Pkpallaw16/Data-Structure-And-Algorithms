class Node:
    def __init__(self,data=0):
        self.data=data
        self.children=[]
def construct(arr):
    root=None
    stack=[]
    for i in range(len(arr)):
        if arr[i]!=None:
            if not stack:
                root=Node(arr[i])
                stack.append(root)
            else:
                node=Node(arr[i])
                stack[-1].children.append(node)
                stack.append(node)
        else:
            stack.pop()
    return root
def display(root):
    print("[",root.data,"]","->",end="")
    str1="["
    for child in root.children:
        str1+=str(child.data)+","
    str1+="]"
    print(str1)
    for child in root.children:
        display(child)
def getTail(node):
    tail=node
    while len(tail.children)!=0:
        tail=tail.children[0]
    return tail
def Linearize_generic_tree(root):
    for child in root.children:
        Linearize_generic_tree(child)
    for i in range(len(root.children)-2,-1,-1):
        last=root.children[i+1]
        slast=root.children[i]
        root.children.pop(i+1)
        tail=getTail(slast)
        tail.children.append(last)
#Linearize with tail
def Linearize_generic_tree_2nd(node):
    if len(node.children)==0:
        return node
    lastnode=node.children[len(node.children)-1]
    tail=Linearize_generic_tree_2nd(lastnode)
    for i in range(len(node.children) - 2, -1, -1):
        rem=node.children.pop(i+1)
        stail=Linearize_generic_tree_2nd(node.children[i])
        stail.children.append(rem)
    return tail

def fun():
    data=[10,20,None,30,50,None,60,None,None,40,None,None]
    root=construct(data)
    display(root)
    Linearize_generic_tree(root)
    display(root)
fun()
