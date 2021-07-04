# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def next_greater_node(arr, head, n):
    stack = []
    res = [0 for i in range(n)]
    temp = head
    i = 0
    while temp != None:
        if not stack:
            stack.append(i)
        else:
            while len(stack) > 0 and arr[stack[-1]].val < arr[i].val:
                res[stack.pop()] = arr[i].val
            stack.append(i)
        i += 1
        temp = temp.next
    for ele in res:
        print(ele, end=" ")


def fun():
    listnode = []
    n = int(input())
    node_value = [int(x) for x in input().split()]
    prev = None
    for i in range(n):
        listnode.append(Node(node_value[i]))
        if prev != None:
            prev.next = listnode[i]
        prev = listnode[i]
    next_greater_node(listnode, listnode[0], n)


fun()