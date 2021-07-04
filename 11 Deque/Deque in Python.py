from _collections import deque
d=deque()
d.append(10)
d.append(20)
d.append(30)
d.appendleft(40)
print(d)
print(d.pop())
print(d.popleft())
print(d)


from _collections import deque
d=deque([10,20,30,40])
d.insert(2,10)
print(d.count(10))
d.remove(10)
print(d)
d.extend([50,60])
print(d)
d.extend([15,25])
print(d)


from _collections import deque
d=deque([10,20,30,40,50])
d.rotate(2)
print(d)
d.rotate(-2)
print(d)
d.reverse()
print(d)


from _collections import deque
d=deque([10,20,30,40,50])
print(d[2])
d[2]=100
print(d)
print(d[0])
print(d[-1])

