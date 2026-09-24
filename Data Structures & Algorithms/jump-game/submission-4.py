class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        farthest = nums[0]

        for i, num in enumerate(nums[1:], 1):

            if i > farthest:
                return False

            farthest = max(farthest, i + num)

            if farthest >= len(nums) - 1:
                return True

        return False