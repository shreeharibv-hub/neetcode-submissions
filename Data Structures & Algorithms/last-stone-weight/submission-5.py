class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x=-heapq.heappop(stones)
            y=-heapq.heappop(stones)

            if x==y:
                continue
            else:
                z=x-y
                heapq.heappush(stones,-z)
        return abs(stones[0]) if stones else  0