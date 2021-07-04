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
predecessor=None
successor=None
state=0
def Predecessor_And_Successor_Element(root,data):
    global predecessor,successor,state
    if state==0:
        if root.data==data:
            state+=1
        else:
            predecessor = root
    elif state==1:
        successor=root
        state+=1
        return
    for child in root.children:
        if state<2:
            Predecessor_And_Successor_Element(child,data)

def fun():
    data=[10,20,None,30,50,None,60,None,None,40,None,None]
    data1=[100,200,None,300,500,None,600,None,None,400,None,None]
    root=construct(data)
    root1 = construct(data1)
    display(root)
    Predecessor_And_Successor_Element(root,30)
    print(predecessor.data,successor.data)
fun()
