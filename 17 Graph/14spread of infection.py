
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
    def number_of_infection(self,src,viisted,t):
        st=[]
        st.append(self.pair(src,1))
        count=0
        while len(st)>0:
            pr=st.pop(0)
            if viisted[pr.ver]!=-1:
                continue
            viisted[pr.ver]=pr.level
            if pr.level>t:
                break
            count+=1
            for edg in self.graph[pr.ver]:
                if viisted[edg.to_ver]==-1:
                    st.append(self.pair(edg.to_ver,pr.level+1))


        print(count,viisted)

    def Input_fun(self):
        edg = int(input("enter number of edges : "))
        for i in range(edg):
            m, n, wt = [int(x) for x in input().split()]
            self.addEdge(m,n,wt)
        self.display()
        visited = [-1 for i in range(len(self.graph))]
        per=int(input("enter infected person "))
        t=int(input("enter time "))
        self.number_of_infection(per, visited,t)

def fun():
    n = int(input("enter number of vertex : "))
    gr = Graph(n)
    gr.Input_fun()
fun()
