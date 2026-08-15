class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        

        for x in strs:
            l=len(x)
            encoded+=str(l)+"#"+x

        return encoded


        
    def decode(self, s: str) -> List[str]:

        decoded=[]
        i=0
        while i<len(s):
            j=s.find("#",i)
            l = int(s[i:j])
            p=s[j+1:j+l+1]
            decoded.append(p)
            i=j+1+l
        return decoded



obj=Solution()
p=obj.encode(strs = ["Hello","World"])
q=obj.decode(s=p)
print(p)
print(q)

            