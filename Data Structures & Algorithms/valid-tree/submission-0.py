class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False

        adj=[[] for _ in range(n)]
        visited=set()
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node,parent):
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour==parent:
                    continue
                if neighbour in visited:
                    return False
                if neighbour not in visited:
                    if not dfs(neighbour, node):
                        return False
            return True
            
        if not dfs(0, -1):
            return False

        return len(visited) == n





        