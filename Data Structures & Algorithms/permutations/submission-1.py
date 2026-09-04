class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=set()
        def backtack(i,path):
            if len(path)==len(nums):
                res.append(path.copy())
                return
            if i==len(nums):
                return

            for x in range(len(nums)):
                if nums[x] not in used:
                    used.add(nums[x])
                    path.append(nums[x])
                    backtack(i+1,path)
                    path.pop()
                    used.remove(nums[x])
        backtack(0,[])
        return res
