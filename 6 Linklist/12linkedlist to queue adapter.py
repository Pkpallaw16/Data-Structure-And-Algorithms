import math
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LLToqueue:
    def __init__(self, head=None, tail=None, size=0):
        self.head = head
        self.tail = tail
        self.size = size

    def addLast(self, key):
        if self.size == 0:
            nn = Node(key)
            self.head = nn
            self.tail = nn
            self.size += 1
        else:
            nn = Node(key)
            self.tail.next = nn
            self.tail = nn
            self.size += 1
    def push(self, x):
        self.addLast(x)

    def size_stack(self):
        return self.size
    def getFirst(self):
        if self.size==0:
            return -1
        return self.head.data
    def peek(self):
        return self.getFirst()

    def removeFirst(self):
        if self.size == 0:
            print("underflow")
            return
        elif self.size == 1:
            val = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return val
        else:
            val = self.head.data
            self.head = self.head.next
            self.size -= 1
            return val
    def pop(self):
        return self.removeFirst()


s=LLToqueue()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.peek())
print(s.size_stack())


