class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = {}

        def string_cmp(m, n):

            if m == len(text1) or n == len(text2):
                return 0

            if (m, n) in dp:
                return dp[(m, n)]

            if text1[m] == text2[n]:
                dp[(m, n)] = 1 + string_cmp(m + 1, n + 1)

            else:
                dp[(m, n)] = max(
                    string_cmp(m + 1, n),
                    string_cmp(m, n + 1)
                )

            return dp[(m, n)]

        return string_cmp(0, 0)