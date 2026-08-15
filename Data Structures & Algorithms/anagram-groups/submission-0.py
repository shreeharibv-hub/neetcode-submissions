
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}

        for x in strs:
            key = "".join(sorted(x))

            if key not in count:
                count[key] = []

            count[key].append(x)

        return list(count.values())


obj = Solution()
p = obj.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
print(p)