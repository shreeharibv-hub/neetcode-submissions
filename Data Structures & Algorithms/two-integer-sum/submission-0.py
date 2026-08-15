from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):

            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i


obj = Solution()
p = obj.twoSum(nums=[3, 4, 5, 6], target=7)
print(p)