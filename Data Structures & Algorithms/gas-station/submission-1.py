class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cg=[]

        for i in range(len(gas)):
            cg.append(gas[i]-cost[i])
        if sum(cg)<0:
            return -1

        p=0
        curr=0
        for i in range(len(gas)):
            curr=curr+cg[i]
            if curr<0:
                p=i+1
                curr=0
        return p
            
            
        