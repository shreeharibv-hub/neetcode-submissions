class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def dfs(n):
            if n == 0:
                return 0
            if n == 1:
                return nums[0]

            if n in dp:
                return dp[n]

            dp[n] = max(nums[n-1] + dfs(n-2), dfs(n-1))
            return dp[n]

        return dfs(len(nums))