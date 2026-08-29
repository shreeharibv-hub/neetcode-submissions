class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        x=len(nums)-k
        return nums[x] 