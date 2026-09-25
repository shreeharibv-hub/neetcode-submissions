class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        q = {}

        for i in range(len(s)):
            q[s[i]] = i

        ans = []
        i = 0

        while i < len(s):
            curr = q[s[i]]
            j = i

            while j <= curr:
                curr = max(curr, q[s[j]])
                j += 1

            ans.append(curr - i + 1)

            i = curr + 1

        return ans