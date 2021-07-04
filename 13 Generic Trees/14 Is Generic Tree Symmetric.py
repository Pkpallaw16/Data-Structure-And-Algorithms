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
def Are_Trees_Mirror_In_Shape(node1,node2):
    if len(node1.children) !=len(node2.children):
        return False
    for i in range(len(node1.children)):
        j=len(node2.children)-i-1
        c1=node1.children[i]
        c2=node2.children[j]
        if Are_Trees_Mirror_In_Shape(c1,c2)==False:
            return False
    return True
def Is_Generic_Tree_Symmetric(root):
    return Are_Trees_Mirror_In_Shape(root,root)
def fun():
    data=[10,20,None,30,50,None,60,None,None,40,None,None]
    data1=[100,200,None,300,500,None,600,None,None,400,None,None]
    root=construct(data)
    root1 = construct(data1)
    display(root)
    print(Is_Generic_Tree_Symmetric(root))
    print(Is_Generic_Tree_Symmetric(root1))
fun()