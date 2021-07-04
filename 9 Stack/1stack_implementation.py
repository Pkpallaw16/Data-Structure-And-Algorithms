class stack:

    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = [0 for i in range(capacity)]

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[self.top]

    def pop(self):
        if not self.isEmpty():
            pop_ele=self.array[self.top]
            self.top -= 1
            return pop_ele
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        if self.top<self.capacity-1:
            self.top += 1
            self.array[self.top]=op
        else:
            print("stack is full")

    def size(self):
        return self.top
    def display(self):
        print(self.array[:self.top+1])

st=stack(5)
print(st.isEmpty())
st.push(4)
st.push(6)
st.push(2)
st.push(3)
st.push(2)
st.push(1)
st.display()
print(st.pop())
print(st.pop())
print(st.peek())
st.display()

