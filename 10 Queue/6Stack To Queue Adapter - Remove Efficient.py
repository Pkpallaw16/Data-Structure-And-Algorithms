from _collections import deque
class stack_To_queue_Adapter:
    def __init__(self):

        self.main_qu=[]
        self.helper=[]

    def push(self,val):

        while len(self.main_qu)>0:
            self.helper.append(self.main_qu.pop())
        self.main_qu.append(val)
        while len(self.helper)>0:
            self.main_qu.append(self.helper.pop())
    def pop(self):
        if len(self.main_qu)==0:
            return -1
        else:
            val = self.main_qu.pop()
            return val
    def top(self):
        if len(self.main_qu) == 0:
            return -1
        else:

            return self.main_qu[-1]
    def display(self):
        print(self.main_qu)
        print(self.helper)

qs=stack_To_queue_Adapter()
qs.push(10)
qs.push(20)
qs.push(30)
qs.push(50)
qs.display()
print(qs.pop())
qs.display()
print(qs.pop())
qs.display()
print(qs.top())
qs.display()