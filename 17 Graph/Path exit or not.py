class Edge:
    def __init__(self,src,nbr,wt):
        self.src=src
        self.nbr=nbr
        self.wt=wt
def paths_source_to_dest(graph,src,dest,visited):
    if src==dest:
        return True
    visited[src]=True
    for edge in graph[src]:
        if visited[edge.nbr]==False:
            if paths_source_to_dest(graph,edge.nbr,dest,visited):
                return True
    return False

vtces=int(input("enter number of vertices"))
edges=int(input("enter number of edges"))
graph=[[]for i in range(vtces)]
for i in range(edges):
    v1,v2,wt=[int(x) for x in input().split()]
    graph[v1].append(Edge(v1,v2,wt))
    graph[v2].append(Edge(v2, v1, wt))
src=int(input("enter source"))
dest=int(input("enter destination"))
visited=[False for i in range(vtces)]
print(paths_source_to_dest(graph,src,dest,visited))
