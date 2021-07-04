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
max=-sys.maxsize
node_data=0
def Node_With_Maximum_Subtree_Sum(root):
    global max,node_data
    sum1=root.data
    for child in root.children:
        sum1+=Node_With_Maximum_Subtree_Sum(child)
    if sum1>max:
        node_data=root.data
        max=sum1
    return sum1
def Subtree_Sum(root):
    sum1=root.data
    for child in root.children:
        sum1+=Subtree_Sum(child)
    print(sum1,root.data)
    return sum1
def fun():
    data=[10,20,None,30,50,None,60,None,None,40,None,None]
    data1=[100,200,None,300,500,None,600,None,None,400,None,None]
    root=construct(data)
    root1 = construct(data1)
    display(root)
    Node_With_Maximum_Subtree_Sum(root)
    print(max,node_data)
    Subtree_Sum(root)


fun()