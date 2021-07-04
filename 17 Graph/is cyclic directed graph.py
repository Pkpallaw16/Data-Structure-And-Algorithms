class Solution:
    def isCycleUtil(self, u, order, adj, vis):
        vis[u] = True
        order[u]=True
        for v in adj[u]:
            if vis[v]==False:
                if(self.isCycleUtil(v, order, adj, vis)):
                    return True
            elif(order[v]):
                return True
        order[u]=False
        return False
    def isCyclic(self, V, adj):
        vis = [False for i in range(V)]
        order=[False for i in range(V)]
        for i in range(V):
            if(vis[i] == False):
                if(self.isCycleUtil(i, order, adj, vis)):
                    return True
        return False