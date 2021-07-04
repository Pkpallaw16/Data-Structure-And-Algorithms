from _collections import deque
class stack_To_queue_Adapter:
    def __init__(self):

        self.main_qu=[]
        self.helper=[]

    def push(self,val):
        self.main_qu.append(val)
    def pop(self):
        if len(self.main_qu)==0:
            return -1
        else:
            while len(self.main_qu)>1:
                self.helper.append(self.main_qu.pop())
            val = self.main_qu.pop()

            while len(self.helper) > 0:
                self.main_qu.append(self.helper.pop())
            self.helper = []
            return val
    def top(self):
        if len(self.main_qu) == 0:
            return -1
        else:
            while len(self.main_qu) > 1:
                self.helper.append(self.main_qu.pop())
            val = self.main_qu.pop()
            self.helper.append(val)
            while len(self.helper) > 0:
                self.main_qu.append(self.helper.pop())
            self.helper = []
            return val
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