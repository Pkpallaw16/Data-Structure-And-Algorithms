class minstack:
    def __init__(self):
        self.alldata=[]
        self.mindata=[]
    def size(self):
        return len(self.alldata)
    def push(self,val):
        self.alldata.append(val)
        if len(self.mindata)>0:
            self.mindata.append(min(self.mindata[-1],val))
        else:
            self.mindata.append(val)
    def pop(self):
        if len(self.alldata)==0:
            print("stack underflow")
            return -1
        else:
            self.mindata.pop()
            return self.alldata.pop()
    def top(self):
        if len(self.alldata)==0:
            print("stack underflow")
            return -1
        else:
            return self.alldata[-1]
    def min(self):
        if len(self.alldata)==0:
            print("stack underflow")
            return -1
        else:
            return self.mindata[-1]
ms=minstack()
ms.push(12)
ms.push(16)
ms.push(8)
ms.push(4)
ms.push(19)
print(ms.mindata)
print(ms.pop())
print(ms.pop())
print(ms.pop())
print(ms.min())
print(ms.mindata)
