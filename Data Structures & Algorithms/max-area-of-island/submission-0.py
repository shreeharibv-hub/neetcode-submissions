class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if grid is None:
            return 0

        used = set()
        max_area = 0

        def dfs(i, j):

            if i < 0 or i >= len(grid):
                return 0

            if j < 0 or j >= len(grid[0]):
                return 0

            if grid[i][j] == 0:
                return 0

            if (i, j) in used:
                return 0

            used.add((i, j))

            area = 1

            area += dfs(i - 1, j)
            area += dfs(i + 1, j)
            area += dfs(i, j - 1)
            area += dfs(i, j + 1)

            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1 and (i, j) not in used:
                    max_area = max(max_area, dfs(i, j))

        return max_area