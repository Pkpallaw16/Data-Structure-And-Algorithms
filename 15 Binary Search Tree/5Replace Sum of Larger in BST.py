class Node:
    def __init__(self,val,left=None,right=None):
        self.data=val
        self.left=left
        self.right=right
def construct(data,lo,hi):
    if lo>hi:
        return None
    mid=(lo+hi)//2
    lc=construct(data,lo,mid-1)
    rc=construct(data,mid+1,hi)
    new_node=Node(data[mid],lc,rc)
    return new_node
def display(root):
    if root==None:
        return
    str1=""
    if root.left==None:
        str1+="."
    else:
        str1 += str(root.left.data)
    str1+="<--"+str(root.data)+"--> "
    if root.right==None:
        str1+="."
    else:
        str1 += str(root.right.data)
    print(str1)
    display(root.left)
    display(root.right)
sum=0
def Replace_Sum_of_Larger_in_BST(root):
    global sum
    if root==None:
        return
    Replace_Sum_of_Larger_in_BST(root.right)
    old_data=root.data
    root.data=sum
    sum+=old_data
    Replace_Sum_of_Larger_in_BST(root.left)

def fun():
    data=[10,20,30,40,50,60,70,80,90]
    root=construct(data,0,len(data)-1)
    display(root)
    print()
    Replace_Sum_of_Larger_in_BST(root)
    display(root)
fun()