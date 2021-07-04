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
    tz=0
    for child in root.children:
        cs=size(child)
        tz=tz+cs
    return tz+1
def maximum(root):
    mx=-sys.maxsize
    for child in root.children:
        mx=max(mx,maximum(child))
    return max(mx,root.data)

def minimum(root):
    mn=sys.maxsize
    for child in root.children:
        mn=min(mn,maximum(child))
    return min(mn,root.data)

def height2(root):
    ht = -1
    for child in root.children:
        ht = max(ht,height2(child))
    return ht + 1
def fun():
    data=[10,20,50,None,60,None,None,30,70,None,80,110,None,120,None,None,90,None,None,40,100,None,None,None]
    root=construct(data)
    display(root)
    print(size(root))
    print(maximum(root))
    print(minimum(root))
    print(height2(root))
fun()

