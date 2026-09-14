class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[None] * n for _ in range(n)]
        count = 0

        def xyz(i, j):
            if i >= j:
                return True

            if dp[i][j] is not None:
                return dp[i][j]

            dp[i][j] = s[i] == s[j] and xyz(i + 1, j - 1)

            return dp[i][j]

        for i in range(n):
            for j in range(i, n):
                if xyz(i, j):
                    count += 1

        return count