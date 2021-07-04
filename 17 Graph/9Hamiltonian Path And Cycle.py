
class pair:
    def __init__(self,path,dist):
        self.path=path
        self.dist =dist
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
            for edge in self.graph[ver]:
                print("[", ver, "]", "-->", "(", edge.from_ver, "<-", edge.to_ver, "@", edge.wt, ")", ",", end=" ")
            print()

    def All_paths(self,src,visited,path,start):
        if len(path)==len(self.graph)-1:
            ham_cycle=False
            for edg in self.graph[src]:
                if edg.to_ver==start:
                    ham_cycle=True
                    break
            if ham_cycle:
                print(path+str(src)+"*")
            else:
                print(path+str(src)+".")
        visited[src]=True
        for edge in self.graph[src]:
            if visited[edge.to_ver]==False:
                self.All_paths(edge.to_ver,visited, path+str(src),start)
        visited[src]=False
    def hamiltonian_path_and_cycle(self):
        edg = int(input("enter number of edges : "))
        for i in range(edg):
            m, n, wt = [int(x) for x in input().split()]
            self.addEdge(m,n,wt)
        self.display()
        visited = [False for i in range(len(self.graph))]
        start_point=int(input("enter number starting vertex : "))
        self.All_paths(start_point, visited, "", start_point)
def fun():
    n = int(input("enter number of vertex : "))
    gr = Graph(n)
    gr.hamiltonian_path_and_cycle()
fun()
