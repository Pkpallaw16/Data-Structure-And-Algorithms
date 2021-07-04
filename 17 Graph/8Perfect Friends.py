
class Edge:
    def __init__(self,v1,v2):
        self.from_ver=v1
        self.to_ver=v2
class Graph:
    def __init__(self,n):
        self.graph=[[] for j in range(n)]

    def addEdge(self, v1, v2):
        self.graph[v1].append(Edge(v1,v2))
        self.graph[v2].append(Edge(v2,v1))

    def display(self):
        for ver in range(len(self.graph)):
            print("[", ver, "]", "-->",end="")
            for edge in self.graph[ver]:
                print( "(", edge.from_ver, "<-", edge.to_ver,  ")", ",", end=" ")
            print()

    def All_paths(self,src,visited,lis):

        visited[src]=True
        lis.append(src)
        for edge in self.graph[src]:
            if visited[edge.to_ver]==False:
                self.All_paths(edge.to_ver, visited,lis)
def perfect_friend(frnd,lis):
    comb_same_club=0
    for club in lis:
        if len(club)>2:
            comb_same_club+=int((len(club)*(len(club)-1))/2)
        elif len(club)==2:
            comb_same_club+=1

    Pf=int(frnd*(frnd-1)/2)-comb_same_club
    return Pf


def fun():
    frnd=int(input("enter number of friend: "))
    gr = Graph(frnd)
    clubs=int(input("enter number of club: "))
    for i in range(clubs):
        m, n = [int(x) for x in input().split()]
        gr.addEdge(m, n)
    gr.display()
    visited = [False for i in range(frnd)]
    connected_components=[]
    component=0
    for i in range(n):

        if visited[i]==False:
            component+=1
            lis = []
            gr.All_paths(i, visited,lis)
            connected_components.append(lis)
    print(connected_components)
    print(perfect_friend(frnd, connected_components))
fun()

def perfect_friend_2nd():
    frnd=int(input("enter number of friends: "))
    clubs=int(input("enter number of clubs : "))
    graph=[[int(x) for x in range(frnd)] for i in range(frnd)]
    visited=[[False for x in range(frnd)] for i in range(frnd)]
    for i in range(1,clubs+1):
        m,n=[int(x) for x in input().split()]
        graph[m][n]=i
        graph[n][m]=i
    count=0
    for i in range(frnd):
        for j in range(frnd):
            if i!=j and visited[i][j]==False and visited[j][i]==False:
                    if graph[i][j]==0 and graph[j][i]==0:
                        count+=1
                        visited[i][j] = True
                        visited[j][i] = True
                    elif graph[i][j]!=graph[j][i]:
                        count += 1
                        visited[i][j] = True
                        visited[j][i] = True

    print(count)
#perfect_friend_2nd()