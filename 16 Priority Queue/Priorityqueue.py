try:
    import Queue as Q
except ImportError:
    import queue as Q

q = Q.PriorityQueue()
q.put(10)
q.put(1)
q.put(5)
while not q.empty():
	print(q.get())


q = Q.PriorityQueue()
q.put((10,'ten'))
q.put((1,'one'))
q.put((5,'five'))
while not q.empty():
    print(q.get())

# giving error in this case

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

class Skill(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New Level:', description)
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q = Q.PriorityQueue()

q.put(Skill(5, 'Proficient'))
q.put(Skill(10, 'Expert'))
q.put(Skill(1, 'Novice'))

while not q.empty():
    next_level = q.get()
    print('Processing level:', next_level.description)