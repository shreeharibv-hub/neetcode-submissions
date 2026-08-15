class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=0
        while l<=r:
            total=0
            mid=(l+r)//2
            for i in range(len(piles)):
                total+=(piles[i]+mid-1)//mid
            if total<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
                
