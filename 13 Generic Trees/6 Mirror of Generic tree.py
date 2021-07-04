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

def mirror(root):
    for child in root.children:
        mirror(child)
    left=0
    right=len(root.children)-1
    while left<right:
        root.children[left],root.children[right]=root.children[right],root.children[left]
        left+=1
        right-=1


def fun():
    data=[10,20,None,30,50,None,60,None,None,40,None,None]
    root=construct(data)
    display(root)
    mirror(root)
    display(root)

fun()