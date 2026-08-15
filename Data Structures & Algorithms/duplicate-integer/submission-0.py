
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count={}
        for x in nums:
            count[x]=count.get(x,0)+1
            if count[x]>1:
                return True
        
        else:
            return False
                    
        
y=Solution()
p=y.hasDuplicate([1, 2, 4, 4])
if(p==True):
    print("true")
elif(p==False):
    print("false")
print(p)