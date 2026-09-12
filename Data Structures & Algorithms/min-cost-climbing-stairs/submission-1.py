class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = {}

        def dfs(n):
            if n == 0:
                return cost[0]
            if n == 1:
                return cost[1]

            if n in dp:
                return dp[n]

            dp[n] = cost[n] + min(dfs(n - 1), dfs(n - 2))
            return dp[n]

        return min(dfs(len(cost) - 1), dfs(len(cost) - 2))