class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(i,path,remain):
            if remain==0:
                res.append(path.copy())
                return
            if remain<0:
                return

            if i==len(nums):
                return

            path.append(nums[i])
            backtrack(i,path,remain-nums[i])
            path.pop()

            backtrack(i+1,path,remain)
        backtrack(0,[],target)
        return res