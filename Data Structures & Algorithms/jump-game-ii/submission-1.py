class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        prev_boundry=0
        boundry=nums[0]
        farthest=0
        jump=1

        while boundry<len(nums)-1:
            for i in range(prev_boundry,boundry+1):
                farthest=max(farthest,i+nums[i])
            prev_boundry=boundry
            boundry=farthest
            jump+=1
        return jump



        