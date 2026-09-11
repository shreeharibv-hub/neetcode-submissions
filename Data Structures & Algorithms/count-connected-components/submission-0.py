class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = set()
        components = 0

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            visited.add(node)

            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components