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
class pair:
    def __init__(self,node,state):
        self.node= node
        self.state=state
def Iterative_preorder_postorder_2nd(root):
    st=[]
    st.append(pair(root,-1))
    pre=""
    post=""
    while len(st)>0:
        top=st[-1]
        if top.state==-1:
            pre+=str(top.node.data)+" "
            top.state+=1
        elif top.state==len(top.node.children):
            post+=str(top.node.data)+" "
            st.pop()
        else:
            cp=pair(top.node.children[top.state],-1)
            st.append(cp)
            top.state+=1
    print("pre: ",pre)
    print("post: ",post)
def fun():
    data=[10,20,50,None,60,None,None,30,70,None,80,110,None,120,None,None,90,None,None,40,100,None,None,None]
    root=construct(data)
    display(root)
    Iterative_preorder_postorder_2nd(root)
fun()