class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums+nums
        return ans

obj=Solution()
p=obj.getConcatenation(nums = [1,4,1,2])
print(p)

        