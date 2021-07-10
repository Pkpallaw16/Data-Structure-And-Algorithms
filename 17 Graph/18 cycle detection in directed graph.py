
class Graph:
    def __init__(self,n):
        self.graph=[[] for j in range(n)]

    def addEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def display(self):
        for ver in range(len(self.graph)):
            print("[", ver, "]", "-->")
            for nbr in self.graph[ver]:
                print("(", ver, "->", nbr,")", ",", end=" ")
            print()

    def cycle_detection_directed_graph(self,src,visited,myapth):
        visited[src]=True
        myapth[src]=True
        for nbr in self.graph[src]:
            if myapth[nbr]==True:
                return True
            elif visited[nbr]==False:
                res=self.cycle_detection_directed_graph(nbr,visited,myapth)
                if res==True:
                    return True
        myapth[src]=False
        return False


    def fun_input(self):
        edg = int(input("enter number of edges : "))
        for i in range(edg):
            m, n= [int(x) for x in input().split()]
            self.addEdge(m,n)
        self.display()
        visited = [False for i in range(len(self.graph))]
        myapth = [False for i in range(len(self.graph))]
        for v in range(len(self.graph)):
            if visited[v]==False:
                res=self.cycle_detection_directed_graph(v,visited,myapth)
                if res==True:
                    return True
        return False

def fun():
    n = int(input("enter number of vertex : "))
    gr = Graph(n)
    print(gr.fun_input())
fun()
