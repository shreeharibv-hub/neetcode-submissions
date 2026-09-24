class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        maximum=nums[0]

        for num in nums[1:]:
            extend=curr+num
            skip=num

            if extend>skip:
                curr=extend
            else:
                curr=num
            maximum=max(maximum,curr)
        return maximum