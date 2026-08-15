from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=Counter(s)
        m=Counter(t)
        if(n==m):
            return True
        else:
           return False

obj=Solution()
p=obj.isAnagram(s = "racecar", t = "carrace")
print(p)
            