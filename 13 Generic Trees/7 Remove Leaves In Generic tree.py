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
def remove_leaf(root):

    for i in range(len(root.children)):
        root.children[i]=remove_leaf(root.children[i])
    if len(root.children)==0:
        return None
    else:
        return root
def remove_leaf_2nd(root):
    for i in range(len(root.children)-1,-1,-1):
        child=root.children[i]
        if len(child.children)==0:
            root.children.pop(i)
    for child in root.children:
        remove_leaf_2nd(child)

def display_remove_leaf(root):
    print("[",root.data,"]","->",end="")
    str1="["
    for child in root.children:
        if child!=None:
            str1+=str(child.data)+","
    str1+="]"
    print(str1)
    for child in root.children:
        if child!=None:
            display_remove_leaf(child)

def fun():
    data=[10,20,None,30,50,None,60,None,None,40,None,None]
    root=construct(data)
    display(root)
    remove_leaf_2nd(root)
    display(root)
    #remove_leaf(root)
    #display_remove_leaf(root)

fun()