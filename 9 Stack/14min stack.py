import sys
class stack:

    def __init__(self):
        #self.capacity = capacity
        # This array is used a stack
        self.array = []
        self.min=sys.maxsize

    def isEmpty(self):
        return True if len(self.array) == 0 else False

    def pop(self):
        if len(self.array) == 0:
            print("stack underflow")
            return -1
        if self.array[-1]<self.min:
            val=self.min
            self.min=2*val-self.array.pop()
            return val
        else:
            return self.array.pop()

    # Push the element to the stack
    def push(self, val):
        if self.min>val:
            self.array.append(val+val-self.min)
            self.min=val
        else:
            self.array.append(val)
    def top(self):
        if len(self.array)==0:
            print("stack underflow")
            return -1
        if self.array[-1]<self.min:
            return self.min
        else:
            self.array[-1]



st=stack()
print(st.isEmpty())
st.push(4)
st.push(6)
st.push(2)
st.push(3)
st.push(2)
st.push(1)
print(st.pop())
print(st.pop())
print(st.top())


