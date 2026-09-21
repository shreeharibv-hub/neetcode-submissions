class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp={}
        def dfs(m,n):
            if m<0 or n<0:
                return 0
            if m==0 and n==0:
                return 1
            if (m,n) in dp:
                return dp[(m,n)]
            dp[(m,n)]=dfs(m-1,n)+dfs(m,n-1)
            return dp[(m,n)]
        return dfs(m-1,n-1)