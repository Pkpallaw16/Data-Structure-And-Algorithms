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
height=0
mn=sys.maxsize
mx=-sys.maxsize
size=0
def Multisolver(root,depth):
    global height,size,mn,mx
    size+=1
    mn=min(mn,root.data)
    mx=max(mx,root.data)
    height=max(height,depth)
    for child in root.children:
        Multisolver(child,depth+1)
class multisolver:
    def __init__(self,mn=sys.maxsize,mx=-sys.maxsize,height=-1,sz=1):
        self.mn = mn
        self.mx = mx
        self.height = height
        self.sz = sz
def multisolver_2nd(root):
    nres=multisolver(root.data,root.data,-1,1)
    for child in root.children:
        rres=multisolver_2nd(child)
        nres.mn=min(nres.mn,rres.mn)
        nres.mx = max(nres.mx, rres.mx)
        nres.height = max(nres.height, rres.height)
        nres.sz+=rres.sz
    nres.height+=1
    return nres
def fun():
    data=[10,20,None,30,50,None,60,None,None,40,None,None]
    data1=[100,200,None,300,500,None,600,None,None,400,None,None]
    root=construct(data)
    root1 = construct(data1)
    display(root)
    Multisolver(root1,0)
    print(height,mx,mn,size)
    res=multisolver_2nd(root1)
    print(res.mn,res.mx,res.sz,res.height)

fun()