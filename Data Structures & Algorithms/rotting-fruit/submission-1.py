class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        q = deque()
        minutes=0
        fresh=0

        # Put ALL treasures into the same queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        while q:
            size=len(q)


            while size:
                i, j = q.popleft()

                if i > 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    q.append((i-1, j))
                    fresh-=1

                if i + 1 < len(grid) and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    q.append((i+1, j))
                    fresh-=1

                if j > 0 and grid[i][j-1] ==1:
                    grid[i][j-1] = 2
                    q.append((i, j-1))
                    fresh-=1

                if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    q.append((i, j+1))
                    fresh-=1
                size-=1
            minutes+=1
            
            if fresh==0:
                return minutes
        return -1