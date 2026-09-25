class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans=[0,0,0]
        for triplet in triplets:
            if (triplet[0]<=target[0] and
            triplet[1]<=target[1] and
            triplet[2]<=target[2]):
                ans[0]=max(ans[0],triplet[0])
                ans[1]=max(ans[1],triplet[1])
                ans[2]=max(ans[2],triplet[2])
        return ans==target

            
        