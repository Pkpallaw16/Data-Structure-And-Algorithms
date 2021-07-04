from _collections import deque
class Queue_To_Stack_Adapter:
    def __init__(self):

        self.main_qu=deque()
        self.helper=deque()

    def push(self,val):
        while len(self.main_qu) > 0:
            self.helper.append(self.main_qu.popleft())
        self.main_qu.append(val)
        while len(self.helper) > 0:
            self.main_qu.append(self.helper.popleft())
        self.helper = deque()

    def pop(self):
        if len(self.main_qu)==0:
            return -1
        else:
            val=self.main_qu.popleft()
            return val

    def top(self):
        if len(self.main_qu) == 0:
            return -1
        else:
            while len(self.main_qu) > 1:
                self.helper.append(self.main_qu.popleft())
            val = self.main_qu.popleft()
            self.helper.append(val)
            self.main_qu = self.helper
            self.helper = deque()
            return val
    def display(self):
        print(self.main_qu)
        print(self.helper)

qs=Queue_To_Stack_Adapter()
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