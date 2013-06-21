class graph_search:
    def __init__(self,g):
        self.graph=g
    def bfs(self,source,desti):
        q=[]
        visited=[]
        q.append(source)
        while len(q) >= 1:
            x=q.pop(0)
            visited.append(x)
            if x == desti:
                return visited
            else:
                if self.graph[x] !=None:
                    q=q+self.graph[x]
    def dfs(self,source,desti):
        s=[]
        visited=[]
        s.append(source)
        while len(s) >=1:
            x=s.pop()
            visited.append(x)
            if x == desti:
                return visited
            else:
                if self.graph[x] !=None:
                    s=s+self.graph[x][::-1]
                    

G={0:[1,2],1:[3,4],2:[5,6],3:[7],4:None,5:None,6:None,7:None}
graph_obj = graph_search(G)
print graph_obj.bfs(0,4)
print graph_obj.dfs(0,4)