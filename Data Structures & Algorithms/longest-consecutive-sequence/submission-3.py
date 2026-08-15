class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        seen=set(nums)
        for x in nums:   
            if x-1 not in seen:
                current=x
                length=1
                while current+1 in seen:
                    current+=1
                    length+=1
                max_len=max(max_len,length)

        return max_len
obj=Solution()
p=obj.longestConsecutive
print(p)
            
