import sys
import heapq
class pair:
    def __init__(self,path,dist):
        self.path=path
        self.dist =dist
    def __lt__(self, other):
        return self.dist < other.dist

    def __repr__(self):
        return f'Node value: {self.path},{self.dist}'
smallest_path=""
smallest_dist=sys.maxsize
largest_path=""
largest_dist=-sys.maxsize
just_larger_dist=sys.maxsize
just_larger_path=""
just_smaller_path=""
just_smaller_dist=-sys.maxsize
hp=[]
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

    def All_paths(self,src,dest,visited,path,dist,criteria_wt,k):
        global smallest_path,largest_path,just_larger_path,just_smaller_path,smallest_dist,largest_dist,just_larger_dist,just_smaller_dist,hp
        if src==dest:
            path=path+str(src)
            if smallest_dist>dist:
                smallest_path=path
                smallest_dist=dist
            if largest_dist<dist:
                largest_dist=dist
                largest_path=path
            if dist>criteria_wt:
                if dist<just_larger_dist:
                    just_larger_dist=dist
                    just_larger_path=path
            if dist<criteria_wt:
                if dist>just_smaller_dist:
                    just_smaller_dist=dist
                    just_smaller_path=path

            if len(hp)<k:
                heapq.heappush(hp,pair(path,dist))
            else:
                pr=hp[0]
                if dist>pr.dist:
                    heapq.heappop(hp)
                    heapq.heappush(hp,pair(path,dist))
        visited[src]=True
        for edge in self.graph[src]:
            if visited[edge.to_ver]==False:
                self.All_paths(edge.to_ver, dest, visited, path+str(src), dist+edge.wt, criteria_wt, k)
        visited[src]=False
def fun():
    n = 7
    gr = Graph(n)
    gr.addEdge(0, 1, 10)
    gr.addEdge(1, 2, 10)
    gr.addEdge(2, 3, 10)
    gr.addEdge(0, 3, 40)
    gr.addEdge(3, 4, 2)
    gr.addEdge(4, 5, 3)
    gr.addEdge(5, 6, 3)
    gr.addEdge(4, 6, 8)
    gr.addEdge(2, 5, 5)
    gr.display()
    visited = [False for i in range(n)]
    gr.All_paths(0, 6, visited, "", 0, 30, 4)
    Kth_largest = heapq.heappop(hp)
    print("Smallest Path =", smallest_path, "@", smallest_dist)
    print("Largest Path = ", largest_path, "@", largest_dist)
    print("Just Larger Path than 30 = ", just_larger_path, "@", just_larger_dist)
    print("Just Smaller Path than 30 =", just_smaller_path, "@", just_smaller_dist)
    print("4th largest path =", Kth_largest.path, "@", Kth_largest.dist)
fun()
