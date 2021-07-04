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
def Traversals_generic_tree(root):
    #node pre
    print("Node pre",root.data)
    for child in root.children:
        print("Edge Pre",root.data,"--",child.data)
        Traversals_generic_tree(child)
        print("Edge post", root.data, "--", child.data)
    #node post
    print("Node post", root.data)


def fun():
    data=[10,20,None,30,50,None,60,None,None,40,None,None]
    root=construct(data)
    display(root)
    Traversals_generic_tree(root)
fun()



