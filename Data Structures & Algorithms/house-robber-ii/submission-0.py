class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_linear(arr):
            dp = {}

            def dfs(i):
                if i >= len(arr):
                    return 0

                if i in dp:
                    return dp[i]

                rob = arr[i] + dfs(i + 2)
                skip = dfs(i + 1)

                dp[i] = max(rob, skip)
                return dp[i]

            return dfs(0)

        if len(nums) == 1:
            return nums[0]

        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )