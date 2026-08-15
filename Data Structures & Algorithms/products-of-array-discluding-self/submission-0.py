class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        prefix = [1] * (len(nums) + 1)
        postfix = [1] * (len(nums) + 1)
        

            
                
        for i in range(len(nums)):
            prefix[i+1]=prefix[i]*nums[i]
             
        for i in range(len(nums)-1,-1,-1):
            postfix[i]=postfix[i+1]*nums[i]

        for i,x in enumerate(nums):


            output.append(prefix[i]*postfix[i+1])

        return output
obj=Solution()
p=obj.productExceptSelf(nums = [1,2,4,6])
print(p)