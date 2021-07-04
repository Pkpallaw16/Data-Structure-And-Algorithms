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
def height(root):
    ht = -1
    for child in root.children:
        ht = max(ht,height(child))
    return ht + 1
def Diameter_Of_Generic_Tree(root):
    mh=-1
    smh=-1
    for child in root.children:
        ht=height(child)
        if ht>=mh:
            smh=mh
            mh=ht
        elif ht>smh:
            smh=ht
    dfc=0 #diameter from child
    for child in root.children:
        dfc=max(Diameter_Of_Generic_Tree(child),dfc)
    return max(dfc,mh+smh+2)
diameter=0
def Diameter1(node):
    global diameter
    maxht=-1
    smaxht=-1
    for child in node.children:
        ht=Diameter1(child)
        if ht>=maxht:
            smaxht=maxht
            maxht=ht
        elif ht>smaxht:
            smaxht=ht
    diameter=max(diameter,maxht+smaxht+2)
    return maxht+1
def fun():
    data=[10,20,50,None,60,None,None,30,70,None,80,110,None,120,None,None,90,None,None,40,100,None,None,None]
    root=construct(data)
    display(root)
    print(Diameter_Of_Generic_Tree(root))
    Diameter1(root)
    print(diameter)
fun()

