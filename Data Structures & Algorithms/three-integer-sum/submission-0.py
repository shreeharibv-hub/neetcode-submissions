class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pq = sorted(nums)
        result = []

        for i in range(len(pq)):

            # Skip duplicate i values
            if i > 0 and pq[i] == pq[i - 1]:
                continue

            l = i + 1
            r = len(pq) - 1

            while l < r:

                total = pq[i] + pq[l] + pq[r]

                if total < 0:
                    l += 1

                elif total > 0:
                    r -= 1

                else:
                    result.append([pq[i], pq[l], pq[r]])

                    l += 1
                    r -= 1

                    
                    while l < r and pq[l] == pq[l - 1]:
                        l += 1

        return result