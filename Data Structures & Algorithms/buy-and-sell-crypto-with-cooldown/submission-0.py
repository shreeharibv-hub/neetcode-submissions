class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def dfs(i):
            if i>=len(prices):
                return 0
            if i in dp:
                return dp[i]
            best=dfs(i+1)
            for k in range (i+1,len(prices)):
                profit=prices[k]-prices[i]+dfs(k+2)
                best=max(best,profit)
            dp[i]=best

            return best
        return dfs(0)

                








        