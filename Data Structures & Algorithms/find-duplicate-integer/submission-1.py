class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans=set()
        for x in nums:
            if x not in ans:
                ans.add(x)
            elif x in ans:
                return x
        return 0

        