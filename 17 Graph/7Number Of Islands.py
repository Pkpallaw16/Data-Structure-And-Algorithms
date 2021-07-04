def is_safe(graph,visited,i,j):
    if i>=0 and j>=0 and i<len(graph) and j<len(graph[0]) and visited[i][j]==False and graph[i][j]==0:
        return True
    else:
        return False
def Is_Island(graph,visited,i,j):
    visited[i][j]=True
    row=[-1,0,1,0]
    col=[0,1,0,-1]
    for opt in range(len(row)):
        if is_safe(graph,visited,i+row[opt],j+col[opt]):
            Is_Island(graph,visited,i+row[opt],j+col[opt])
def number_of_island():
    n=int(input("enter row: "))
    m=int(input("enter col: "))
    graph=[[int(x) for x in input().split()] for i in range(m)]
    visited=[[False for x in range(n)] for i in range(m)]
    count=0
    for i in range(m):
        for j in range(n):
            if visited[i][j]==False and graph[i][j]==0:
                count+=1
                Is_Island(graph,visited,i,j)
    print(count)
number_of_island()