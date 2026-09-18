class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        old_min=nums[0]
        old_max=nums[0]
        answer=nums[0]

        for num in nums[1:]:
            curr_max=old_max
            curr_min=old_min

            maximum=max(num,num*curr_max,num*curr_min)
            minimum=min(num,num*curr_max,num*curr_min)
            old_max = maximum
            old_min = minimum
            answer=max(answer,maximum)
        return answer

        