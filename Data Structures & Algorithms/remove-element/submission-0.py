class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for x in nums:

            if val!=x:
                nums[k]=x
                k+=1

        return k
            
    

obj = Solution()
p = obj.removeElement(nums = [3,2,2,3], val = 3)
print(p)