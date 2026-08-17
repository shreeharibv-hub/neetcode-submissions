class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        l=0
        heap=[]
        for r in range(len(nums)):
            heapq.heappush(heap,(-nums[r],r))
            if r-l+1==k:
                while heap[0][1] < l:
                    heapq.heappop(heap)
                max_value = -heap[0][0]
                ans.append(max_value)
                l+=1
            
            
        return ans


        