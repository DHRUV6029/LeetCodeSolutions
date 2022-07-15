class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [True for x in range(0 , len(graph))]  # initially all nodes are White
        visited = set()
        self.isPartite = True

        def dfs(graph , visited, color, v):
            if not self.isPartite:
                return
            visited.add(v)
            
            for n in graph[v]:

                #if neighbour is not visited
                if n not in visited:
                    color[n] = not color[v]

                    dfs(graph, visited , color, n)
                else:
                    if color[n] == color[v]:
                        self.isPartite = False

            return True

        for x in range(0, len(graph)):
            if x not in visited:
                dfs(graph, visited, color, x)

        return(self.isPartite)