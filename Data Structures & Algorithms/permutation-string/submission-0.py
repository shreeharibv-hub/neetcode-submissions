class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count={}
        for i in range(len(s1)):
            count[s1[i]]=count.get(s1[i],0)+1
        l=0
        freq={}
        for r in range(len(s2)):
            freq[s2[r]]=freq.get(s2[r],0)+1
            if (r-l+1)==len(s1):
                if freq==count:
                    return True
                freq[s2[l]]-=1

                if freq[s2[l]]==0:
                    del(freq[s2[l]])
                l+=1
        return False



        
        