class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        # Always binary search on smaller array
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        l = 0
        r = n1

        left = (n1 + n2 + 1) // 2

        while l <= r:
            mid1 = (l + r) // 2
            mid2 = left - mid1

            # Elements immediately left of partitions
            l1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            l2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")

            # Elements immediately right of partitions
            r1 = nums1[mid1] if mid1 < n1 else float("inf")
            r2 = nums2[mid2] if mid2 < n2 else float("inf")

            # Correct partition
            if l1 <= r2 and l2 <= r1:

                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)

            # We took too many elements from nums1
            elif l1 > r2:
                r = mid1 - 1

            # We took too few elements from nums1
            else:
                l = mid1 + 1