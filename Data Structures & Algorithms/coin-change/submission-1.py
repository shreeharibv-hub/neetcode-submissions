class Solution:
    def coinChange(self, coins, amount):
        dp = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount in dp:
                return dp[amount]

            minimum = float('inf')

            for coin in coins:
                rem = amount - coin

                if rem >= 0:
                    result = dfs(rem)

                    if result != float('inf'):
                        minimum = min(minimum, result + 1)

            dp[amount] = minimum
            return minimum

        ans = dfs(amount)

        if ans == float('inf'):
            return -1

        return ans