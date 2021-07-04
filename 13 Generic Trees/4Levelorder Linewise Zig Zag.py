import sys
class Node:
    def __init__(self, value=0):
        self.data = value
        self.children= []
def construct(arr):
    root=None
    st=[]
    for i in range(len(arr)):
        data=arr[i]

        if data!=None:
            nn = Node(data)
            if len(st)==0:
                root=nn
                st.append(nn)
            else:
                st[-1].children.append(nn)
                st.append(nn)
        else:
            st.pop()
    return root

def display(root):
    str1="["+str(root.data)+"] ->"
    for child in root.children:
        str1 +=str(child.data)+","
    print(str1,".")
    for i in range(len(root.children)):
        child=root.children[i]
        display(child)
def size(root):
    sz=0
    for child in root.children:
        sz+=size(child)
    return sz+1
def printing_zigzag(root):
    cur_level=[]
    next_level=[]
    ltr=True
    cur_level.append(root)
    while len(cur_level)>0:
        node=cur_level.pop()
        print(node.data,end=" ")
        if ltr:
            for n in node.children:
                next_level.append(n)
        else:
            for n in range(len(node.children)-1,-1,-1):
                next_level.append(node.children[n])
        if len(cur_level)==0:
            print()
            ltr=not ltr
            cur_level, next_level= next_level,cur_level

def fun():
    data=[10,20,50,None,60,None,None,30,70,None,80,110,None,120,None,None,90,None,None,40,100,None,None,None]
    root=construct(data)
    display(root)
    print(size(root))
    print(printing_zigzag(root))
fun()

