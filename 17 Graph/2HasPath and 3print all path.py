class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class graph:
    def addEdge(self,grph,v1,v2,wt):
        grph[v1].append(Edge(wt,v1,v2))
        grph[v2].append(Edge(wt,v2,v1))

    def display(self,grph):
        for i in range(len(grph)):
            for edge in grph[i]:
                print("[",i,"]","-->","(",edge.node_from,"<-",edge.node_to,"@",edge.value,")",",",end=" ")
            print()
    #dfs----> depth first search
    def hasPath(self,grph,src,dest,visited):
        if src==dest:
            return True
        visited[src]=True
        for edge in grph[src]:
            nbr=edge.node_to
            if visited[nbr]==False:
                res=self.hasPath(grph,nbr,dest,visited)
                if res==True:
                    return True
        return False
    def AllPath_src_dest(self,grph,src,dest,visited,path,dist):
        if src==dest:
            print(path+str(src),"@",dist)
            visited[src]=False
            return
        visited[src]=True
        for edge in grph[src]:
            nbr=edge.node_to
            if visited[nbr]==False:
                self.AllPath_src_dest(grph,nbr,dest,visited,path+str(src),dist+edge.value)
        visited[src]=False

    def fun(self):
        n=7
        grph=[None for i in range(n)]
        for i in range(n):
            grph[i]=[]

        self.addEdge(grph,0,1,10)
        self.addEdge(grph, 1, 2, 10)
        self.addEdge(grph, 2, 3, 10)
        self.addEdge(grph, 0, 3, 10)

        self.addEdge(grph, 3, 4, 10)
        self.addEdge(grph, 4, 5, 10)
        self.addEdge(grph, 5, 6, 10)
        self.addEdge(grph, 4, 6, 10)
        print(grph)
        self.display(grph)
        visited=[False for i in range(n)]
        print(self.hasPath(grph, 0, 6, visited))
        visited = [False for i in range(n)]
        self.AllPath_src_dest(grph, 0, 6, visited,"",0)

gr=graph()
gr.fun()




