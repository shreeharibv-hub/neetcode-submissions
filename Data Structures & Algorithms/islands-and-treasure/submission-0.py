from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        q = deque()

        # Put ALL treasures into the same queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            curr = grid[i][j]

            if i > 0 and grid[i-1][j] == 2147483647:
                grid[i-1][j] = curr + 1
                q.append((i-1, j))

            if i + 1 < len(grid) and grid[i+1][j] == 2147483647:
                grid[i+1][j] = curr + 1
                q.append((i+1, j))

            if j > 0 and grid[i][j-1] == 2147483647:
                grid[i][j-1] = curr + 1
                q.append((i, j-1))

            if j + 1 < len(grid[0]) and grid[i][j+1] == 2147483647:
                grid[i][j+1] = curr + 1
                q.append((i, j+1))