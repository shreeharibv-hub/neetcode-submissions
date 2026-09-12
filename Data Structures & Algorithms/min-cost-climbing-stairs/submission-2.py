class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}

        def dfs(n):
            if n == 0:
                return 0
            if n == 1:
                return 0

            if n in dp:
                return dp[n]

            dp[n] = min(
                cost[n-1] + dfs(n-1),
                cost[n-2] + dfs(n-2)
            )

            return dp[n]

        return dfs(len(cost))