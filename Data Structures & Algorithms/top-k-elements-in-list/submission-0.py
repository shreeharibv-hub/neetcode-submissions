class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        s=(sorted(count.items(), key=lambda x:x[1],reverse=True))
        return [x[0] for x in s[:k]]


obj=Solution()
p=obj.topKFrequent(nums = [1,2,2,3,3,3], k = 2)
print(p)