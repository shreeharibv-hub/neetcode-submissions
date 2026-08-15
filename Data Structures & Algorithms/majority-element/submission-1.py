class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for x in nums:
            count[x]=count.get(x,0)+1
        m=max(count.items(), key=lambda x:x[1])
        return m[0]