
class Edge:
    def __init__(self,v1,v2):
        self.from_ver=v1
        self.to_ver=v2

class Graph:
    def __init__(self,n):
        self.graph=[[] for j in range(n)]

    def addEdge(self, v1, v2):
        self.graph[v1].append(Edge(v1,v2))


    def display(self):
        for ver in range(len(self.graph)):
            print("[", ver, "]", "-->")
            for edge in self.graph[ver]:
                print("(", edge.from_ver, "<-", edge.to_ver,")", ",", end=" ")
            print()

    def topological_sort(self,src,visited,st):
        visited[src]=True
        for nbr in self.graph[src]:
            if visited[nbr.to_ver]==False:
                self.topological_sort(nbr.to_ver,visited,st)
        st.append(src)

    def fun_input(self):
        edg = int(input("enter number of edges : "))
        for i in range(edg):
            m, n= [int(x) for x in input().split()]
            self.addEdge(m,n)
        self.display()
        st=[]
        visited = [False for i in range(len(self.graph))]
        for v in range(len(self.graph)):
            if visited[v]==False:
                self.topological_sort(v,visited,st)
        while len(st)>0:
            print(st.pop(),end=" ")

def fun():
    n = int(input("enter number of vertex : "))
    gr = Graph(n)
    gr.fun_input()
fun()
