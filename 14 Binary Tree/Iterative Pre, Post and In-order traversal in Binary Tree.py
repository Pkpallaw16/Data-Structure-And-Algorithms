from collections import deque
import sys
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class pair:
    def __init__(self,node,state):
        self.node=node
        self.state=state
def display(node):
    if node==None:
        return
    str1=""
    if node.left==None:
        str1 +="."
    else:
        str1 +=str(node.left.value)+""
    str1 += " <-"+str(node.value)+"-> "
    if node.right==None:
        str1 +="."
    else:
        str1 +=str(node.right.value)+""
    print(str1)
    display(node.left)
    display(node.right)

def binary_tree_constructor():
    arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    stack = deque()
    root = Node(arr[0])
    root_pair = pair(root, 1)
    stack.append(root_pair)
    idx = 0
    while len(stack) > 0:
        top = stack[len(stack) - 1]
        if top.state == 1:
            idx += 1
            if arr[idx] != None:
                new_node = Node(arr[idx])
                top.node.left = new_node
                new_pair = pair(new_node, 1)
                stack.append(new_pair)
            else:
                top.node.left = None
            top.state += 1
        elif top.state == 2:
            idx += 1
            if arr[idx] != None:
                new_node = Node(arr[idx])
                top.node.right = new_node
                new_pair = pair(new_node, 1)
                stack.append(new_pair)
            else:
                top.node.right = None
            top.state += 1
        else:
            stack.pop()
    return root
def iterative_pre_post_inorder_traversal(root):
    pre=[]
    inorder=[]
    post=[]
    stack = deque()
    root_pair = pair(root, 1)
    stack.append(root_pair)
    while len(stack) > 0:
        top = stack[len(stack) - 1]
        if top.state == 1:
            pre.append(top.node.value)
            if top.node.left != None:
                new_pair = pair(top.node.left, 1)
                stack.append(new_pair)
            top.state += 1
        elif top.state == 2:
            inorder.append(top.node.value)
            if top.node.right != None:
                new_pair = pair(top.node.right, 1)
                stack.append(new_pair)
            top.state += 1
        else:
            post.append(top.node.value)
            stack.pop()
    print(pre)
    print(inorder)
    print(post)



root=binary_tree_constructor()
display(root)
iterative_pre_post_inorder_traversal(root)




