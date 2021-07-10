
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
        def __init__(self,ver,dis_from_source):
            self.ver=ver
            self.dis_from_source=dis_from_source
    def Is_cyclic(self,src,visited):
        st=[]
        st.append(self.pair(src,str(src)))
        while len(st)>0:
            pr=st.pop(0)
            if visited[pr.ver]==True:
                print(pr.dis_from_source)
                return True
                break
            visited[pr.ver]=True
            for edg in self.graph[pr.ver]:
                if visited[edg.to_ver]==False:
                    st.append(self.pair(edg.to_ver,pr.dis_from_source+str(edg.to_ver)))
        return False
    def Is_cyclic_using_Dfs(self,src,visited):

        visited[src]=True
        for edge in self.graph[src]:
            nbr=edge.to_ver
            if visited[nbr]==True and nbr !=par:
                return True

        for edge in self.graph[src]:
            if visited[edge.to_ver]==False:
                res=self.All_paths(edge.to_ver, visited,src)
                if res==True:
                    return True
    def Input_fun(self):
        edg = int(input("enter number of edges : "))
        for i in range(edg):
            m, n, wt = [int(x) for x in input().split()]
            self.addEdge(m,n,wt)
        self.display()
        visited = [False for i in range(len(self.graph))]

        for i in range(len(visited)):
            if visited[i]==False:
                print(self.Is_cyclic(i, visited))
def fun():
    n = int(input("enter number of vertex : "))
    gr = Graph(n)
    gr.Input_fun()
fun()
