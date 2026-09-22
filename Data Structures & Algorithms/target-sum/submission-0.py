class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, remaining):

            if i==len(nums) and remaining == 0:
                return 1

            if i == len(nums) and remaining!=0:
                return 0

            if (i, remaining) in dp:
                return dp[(i, remaining)]

            Way1 = dfs(i+1, remaining - nums[i])   # take coin
            Way2 = dfs(i + 1, remaining+nums[i])          # skip coin

            dp[(i, remaining)] = Way1 + Way2

            return dp[(i, remaining)]

        return dfs(0, target)