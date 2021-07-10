
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
    class pair:
        def __init__(self,ver,level):
            self.ver=ver
            self.level=level
    def Is_graph_bipatited(self,src,discover_level):
        st=[]
        st.append(self.pair(src,0))
        while len(st)>0:
            pr=st.pop(0)
            if discover_level[pr.ver]!=-1:
                if discover_level[pr.ver]==pr.level:
                    continue
                else:
                    return False

            discover_level[pr.ver]=pr.level

            for edg in self.graph[pr.ver]:
                if discover_level[edg.to_ver]==-1:
                    st.append(self.pair(edg.to_ver,pr.level+1))
        return False

    def Input_fun(self):
        edg = int(input("enter number of edges : "))
        for i in range(edg):
            m, n, wt = [int(x) for x in input().split()]
            self.addEdge(m,n,wt)
        self.display()
        discovery = [-1 for i in range(len(self.graph))]

        for i in range(len(discovery)):
            if discovery[i]==-1:
                res=self.Is_graph_bipatited(i, discovery)
                if res==False:
                    return False
        return True
def fun():
    n = int(input("enter number of vertex : "))
    gr = Graph(n)
    print(gr.Input_fun())
fun()
