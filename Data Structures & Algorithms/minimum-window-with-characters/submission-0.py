class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count={}
        for i  in range(len(t)):
            count[t[i]]=count.get(t[i],0)+1
        have=0
        l=0
        min_count=99999
        freq={}
        ans=""
        need=len(count)

        for r,x in enumerate(s):
            freq[s[r]]=freq.get(s[r],0)+1

            if x in count and count[x]==freq[x]:
                have+=1
            while need==have:
                if r-l+1<min_count:
                    min_count=r-l+1
                    ans=s[l:r+1]
                freq[s[l]]-=1

                if s[l] in count and freq[s[l]]<count[s[l]]:
                    have-=1
                l+=1

        return ans

        