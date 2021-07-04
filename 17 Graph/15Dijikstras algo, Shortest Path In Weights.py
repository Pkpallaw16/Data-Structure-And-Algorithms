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
    class Dpair:
        def __init__(self,ver,psf,wsf):
            self.ver=ver
            self.psf=psf
            self.wsf=wsf

        def __lt__(self, other):
            return self.wsf < other.wsf
    def Dijikstras(self,src,visited):
        st=[]
        heapq.heappush(st,self.Dpair(src,str(src),0))

        while len(st)>0:
            pr=heapq.heappop(st)
            if visited[pr.ver] == True:
                continue
            visited[pr.ver] = True
            print(pr.ver,"via",pr.psf,"@",pr.wsf)
            for edg in self.graph[pr.ver]:
                nbr=edg.to_ver
                if visited[nbr]==False:
                    heapq.heappush(st,self.Dpair(nbr,pr.psf+str(nbr),pr.wsf+edg.wt))

    def fun_input(self):
        edg = int(input("enter number of edges : "))
        for i in range(edg):
            m, n, wt = [int(x) for x in input().split()]
            self.addEdge(m,n,wt)
        self.display()
        visited = [False for i in range(len(self.graph))]
        start_point=int(input("enter starting vertex : "))
        self.Dijikstras(start_point, visited)
def fun():
    n = int(input("enter number of vertex : "))
    gr = Graph(n)
    gr.fun_input()
fun()
