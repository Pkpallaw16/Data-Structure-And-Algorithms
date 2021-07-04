class Evaluate_division:
    class Edge:
        def __init__(self,nbr,wt):
            self.nbr=nbr
            self.wt=wt
    def addedge(self,graph,v1,v2,wt):
        if v1 in graph:
            graph[v1].append(self.Edge(v2,wt))
        else:
            graph[v1]=[self.Edge(v2,wt)]
        if v2 in graph:
            graph[v2].append(self.Edge(v1,float("{0:.2f}".format(1/wt))))
        else:
            graph[v2]=[self.Edge(v1,float("{0:.2f}".format(1/wt)))]
    def Display(self,graph):
        for ver in graph.keys():
            print("[", ver, "]", "->",end=" ")
            for edg in graph[ver]:
                print("(",edg.nbr,edg.wt,")",end=" ")
            print()
    def dfs(self,graph,src,dst,vis,res,qi,cost):
        if src==dst:
            res[qi]=cost
            return True
        vis.append(src)
        for edge in graph[src]:
            if edge.nbr not in vis:
                rres=self.dfs(graph,edge.nbr,dst,vis,res,qi,cost*edge.wt)
                if rres==True:
                    return True
        return False

    def calcEquation(self,equations,values,queries):
        graph={}
        for e in range(len(equations)):
            v1=equations[e][0]
            v2=equations[e][1]
            wt=values[e]
            self.addedge(graph,v1,v2,wt)
        self.Display(graph)
        print(graph)
        res=[0 for x in range(len(queries))]
        for qi in range(len(queries)):
            v1=queries[qi][0]
            v2=queries[qi][1]
            if v1 not in graph or v2 not in graph:
                res[qi]=-1.0
            elif v1==v2:
                res[qi]=1.0
            else:
                vis=[]
                rres=self.dfs(graph,v1,v2,vis,res,qi,1.0)
                if rres==False:
                    res[qi]=-1.0
        return res
    def fun(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        print(self.calcEquation(equations,values,queries))

eq_div=Evaluate_division()
eq_div.fun()