class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        used=set()
        count=0
        def dfs(i,j):
            if i>=len(grid) or i<0:
                return
            if j>=len(grid[0]) or j<0:
                return
            if grid[i][j]=="0":
                return
            if (i, j) in used:
                return
            
            
            used.add((i,j))

            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in used:
                    count+=1
                    dfs(i,j)
        

        return count
                    
            



        