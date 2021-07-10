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
            print("[", ver, "]", "-->",end=" ")
            for edge in self.graph[ver]:
                print("(", edge.from_ver, "->", edge.to_ver, "@", edge.wt, ")", ",", end=" ")
            print()

    #dfs----> depth first search
    def Is_graph_cyclic_dfs(self,src,parent,visited):
        visited[src]=True
        for edge in self.graph[src]:
            nbr=edge.to_ver
            if visited[nbr]==True and nbr!=parent:
                return True
            if visited[nbr]==False:
                res=self.Is_graph_cyclic_dfs(nbr,src,visited)
                if res==True:
                    return True

        return False

    def fun_input(self):
        edg = int(input("enter number of edges : "))
        for i in range(edg):
            m, n, wt = [int(x) for x in input().split()]
            self.addEdge(m, n, wt)
        self.display()
        visited = [False for i in range(len(self.graph))]
        cycle=False
        for ver in range(n):
            if visited[ver]==False:
                cycle=self.Is_graph_cyclic_dfs(0, -1, visited)
                if cycle==True:
                    print(True)
                    break
        if cycle==False:
            print(False)
n = int(input("enter number of vertex : "))
gr=Graph(n)
gr.fun_input()




