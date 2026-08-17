class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        let = set()
        l=0

        for r in range(len(s)):
            while s[r] in let:
                let.remove(s[l])
                l+=1
                
            let.add(s[r])
            max_count=max(max_count,r-l+1)

        return max_count
