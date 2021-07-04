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

def Level_order_Traversals_generic_tree(root):
    #node pre
    next_level=[]
    cur_level=[]
    cur_level.append(root)
    lvl=1
    print("level-",lvl,":",end=" ")
    while cur_level:
        node=cur_level.pop(0)
        print(node.data,end=" ")
        for n in node.children:
            next_level.append(n)
        if len(cur_level) == 0:
            print()
            lvl+=1
            cur_level, next_level = next_level, cur_level
            if len(cur_level)!=0:
                print("level-", lvl, ":", end=" ")
def Level_order_Traversals_generic_tree_2nd(root):
    #node pre
    stack=[]
    stack.append(root)
    stack.append(None)
    while stack:
        node = stack.pop(0)
        if node==None:
            print()
            if len(stack)>0:
                stack.append(None)
        else:
            print(node.data,end=" ")
            for child in node.children:
                stack.append(child)
def Level_order_Traversals_generic_tree_3rd(root):
    #node pre
    stack=[]
    stack.append(root)
    sz=0
    while stack:
        node = stack.pop(0)
        print(node.data,end=" ")
        for child in node.children:
            stack.append(child)
        if sz==0:
            sz=len(stack)
            print()
        sz-=1
def Level_order_Traversals_generic_tree_4rd(root):
    #node pre
    stack=[]
    stack.append(root)
    while stack:
        sz = len(stack)
        while sz>0:
            node = stack.pop(0)
            print(node.data, end=" ")
            for child in node.children:
                stack.append(child)
            sz -= 1
        print()

def fun():
    data=[10,20,None,30,50,None,60,None,None,40,None,None]
    root=construct(data)
    display(root)
    Level_order_Traversals_generic_tree(root)
    Level_order_Traversals_generic_tree_2nd(root)
    Level_order_Traversals_generic_tree_3rd(root)
    Level_order_Traversals_generic_tree_4rd(root)
fun()



