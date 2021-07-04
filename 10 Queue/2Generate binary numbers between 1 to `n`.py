from collections import deque
def generate(n):
    q = deque()
    q.append('1')
    st=[]
    for i in range(n):
        front = str(q.popleft())
        st.append(front)

        q.append(front + '0')
        q.append(front + '1')

    return st

print(generate(16))
