class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, remaining):

            if remaining == 0:
                return 1

            if remaining < 0 or i == len(coins):
                return 0

            if (i, remaining) in dp:
                return dp[(i, remaining)]

            Way1 = dfs(i, remaining - coins[i])   # take coin
            Way2 = dfs(i + 1, remaining)          # skip coin

            dp[(i, remaining)] = Way1 + Way2

            return dp[(i, remaining)]

        return dfs(0, amount)