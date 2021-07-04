import heapq
class Edge:
    def __init__(self,v1,v2,wt):
        self.from_ver=v1
        self.to_ver=v2
        self.wt=wt
class Graph:
    def __init__(self,n):
        self.graph=[[] for j in range(n)]

    def addEdge(self, v1, v2, wt):
        self.graph[v1].append(Edge(v1,v2,wt))
        self.graph[v2].append(Edge(v2,v1,wt))

    def display(self):
        for ver in range(len(self.graph)):
            print("[", ver, "]", "-->")
            for edge in self.graph[ver]:
                print("(", edge.from_ver, "<-", edge.to_ver, "@", edge.wt, ")", ",", end=" ")
            print()
    class Primspair:
        def __init__(self,ver,parent,wt):
            self.ver=ver
            self.parent=parent
            self.wt=wt

        def __lt__(self, other):
            return self.wt < other.wt

    def prims(self,visited):
        st = []
        heapq.heappush(st, self.Primspair(0, -1, 0))
        mst=Graph(len(self.graph))
        while len(st) > 0:
            removal = heapq.heappop(st)
            if visited[removal.ver] == True:
                continue
            visited[removal.ver] = True
            if removal.parent!=-1:
                print("[",removal.ver, "-", removal.parent, "@", removal.wt,"]")
                mst.addEdge(removal.ver,removal.parent,removal.wt)
            for edg in self.graph[removal.ver]:
                nbr = edg.to_ver
                if visited[nbr] == False:
                    heapq.heappush(st, self.Primspair(nbr, removal.ver,edg.wt))
        mst.display()
    def fun_input(self):
        edg = int(input("enter number of edges : "))
        for i in range(edg):
            m, n, wt = [int(x) for x in input().split()]
            self.addEdge(m,n,wt)
        self.display()
        visited = [False for i in range(len(self.graph))]
        self.prims(visited)
def fun():
    n = int(input("enter number of vertex : "))
    gr = Graph(n)
    gr.fun_input()
fun()
