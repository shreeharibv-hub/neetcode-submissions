class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        for a, b in edges:

            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return [a, b]

            parent[rootA] = rootB