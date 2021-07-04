class stack:

    def __init__(self,capacity):
        self.tos1 = -1
        self.tos2=capacity
        self.capacity = capacity
        # This array is used a stack
        self.array = [None for i in range(capacity)]
    def size1(self):
        return self.tos1+1
    def size2(self):
        return self.capacity-self.tos2

    def peek1(self):
        if self.tos1==-1:
            print("stack underflow")
            return -1
        return self.array[self.tos1]
    def peek2(self):
        if self.tos2==self.capacity:
            print("stack underflow")
            return -1
        return self.array[self.tos2]

    def pop1(self):
        if self.tos1!=-1:
            pop_ele=self.array[self.tos1]
            self.tos1 -= 1
            return pop_ele
        else:
            print("underflow")
            return -1
    def pop2(self):
        if self.tos2!=self.capacity:
            pop_ele=self.array[self.tos2]
            self.tos2 += 1
            return pop_ele
        else:
            print("underflow")
            return -1
    # Push the element to the stack
    def push1(self, op):
        if self.tos1+1<self.tos2:
            self.tos1 += 1
            self.array[self.tos1]=op
        else:
            print("stack is full")
    def push2(self, op):
        if self.tos1+1<self.tos2:
            self.tos2 -= 1
            self.array[self.tos2]=op
        else:
            print("stack is full")


st=stack(8)
st.push1(4)
st.push2(6)
st.push1(2)
st.push1(3)
st.push2(2)
st.push2(1)
print(st.pop1())
print(st.pop2())
print(st.peek1())
print(st.peek2())
st.push1(10)
print(st.array)


