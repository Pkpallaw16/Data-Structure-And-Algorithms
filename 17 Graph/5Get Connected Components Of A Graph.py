
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
            print("[", ver, "]", "-->",end="")
            for edge in self.graph[ver]:
                print( "(", edge.from_ver, "<-", edge.to_ver, "@", edge.wt, ")", ",", end=" ")
            print()

    def All_paths(self,src,visited,lis):

        visited[src]=True
        lis.append(src)
        for edge in self.graph[src]:
            if visited[edge.to_ver]==False:
                self.All_paths(edge.to_ver, visited,lis)

def fun():
    n = 7
    gr = Graph(n)
    gr.addEdge(0, 1, 10)
    gr.addEdge(2, 3, 10)
    gr.addEdge(4, 5, 10)
    gr.addEdge(5, 6, 10)
    gr.addEdge(4, 6, 10)
    gr.display()
    visited = [False for i in range(n)]
    connected_components=[]
    component=0
    for i in range(n):

        if visited[i]==False:
            component+=1
            lis = []
            gr.All_paths(i, visited,lis)
            connected_components.append(lis)
    if component==1:
        print("Graph is connected")
    else:
        print("Graph is not connect")
    print(connected_components)

fun()
