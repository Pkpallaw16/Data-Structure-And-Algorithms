
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
    class pair:
        def __init__(self,ver,psf):
            self.ver=ver
            self.psf=psf
    def Iterative_Dfs(self,src,visited):
        st=[]
        st.append(self.pair(src,str(src)))

        while len(st)>0:
            pr=st.pop()
            if visited[pr.ver] == True:
                continue
            visited[pr.ver] = True
            print(pr.ver,"@",pr.psf)
            for edg in self.graph[pr.ver]:
                if visited[edg.to_ver]==False:
                    st.append(self.pair(edg.to_ver,pr.psf+str(edg.to_ver)))

    def fun_input(self):
        edg = int(input("enter number of edges : "))
        for i in range(edg):
            m, n, wt = [int(x) for x in input().split()]
            self.addEdge(m,n,wt)
        self.display()
        visited = [False for i in range(len(self.graph))]
        start_point=int(input("enter starting vertex : "))
        self.Iterative_Dfs(start_point, visited)
def fun():
    n = int(input("enter number of vertex : "))
    gr = Graph(n)
    gr.fun_input()
fun()
