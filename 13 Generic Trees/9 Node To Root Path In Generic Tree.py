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

def Node_to_root_path(root,val):
    if root.data==val:
        bres=[]
        bres.append(root.data)
        return bres
    lis=[]
    for child in root.children:
        lis= Node_to_root_path(child,val)
        if len(lis)>0:
            lis.append(root.data)
            return lis
    return lis
def fun():
    data=[10,20,50,None,60,None,None,30,70,None,80,110,None,120,None,None,90,None,None,40,100,None,None,None]
    root=construct(data)
    display(root)
    print(Node_to_root_path(root,20))
fun()

