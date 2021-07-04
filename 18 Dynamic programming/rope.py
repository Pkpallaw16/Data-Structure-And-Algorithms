def bfs(graph, origin):
    # your code
    visited = {key:False for key in graph.keys()}
    st = []
    st.append(origin)
    while len(st) > 0:
        rem = st.pop(0)
        if visited[rem] == True:
            continue
        print(rem, end=" ")
        visited[rem] = True
        for nbr in graph[rem]:
            if visited[nbr] == False:
                st.append(nbr)
graph={0: [1, 2], 1: [2], 2: [0, 3], 3: [], 8: [9], 9: []}
bfs(graph,2)