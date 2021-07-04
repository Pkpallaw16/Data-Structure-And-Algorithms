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
sum=0
def Replace_sum_of_larger_value(root):
    global sum
    if root == None:
        return
    Replace_sum_of_larger_value(root.right)
    node_value=root.data
    root.data=sum
    sum+=node_value
    Replace_sum_of_larger_value(root.left)
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

def fun():
    data=[10,20,30,40,50,60,70,80,90]
    root=construct(data,0,len(data)-1)
    display(root)
    Replace_sum_of_larger_value(root)
    display(root)
fun()