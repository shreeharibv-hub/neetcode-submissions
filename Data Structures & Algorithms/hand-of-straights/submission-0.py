class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        hand=sorted(hand)
        count={}
        for i in hand:
            count[i]=count.get(i,0)+1
        freq=0
        while count:
            y = min(count)
            for i in range(groupSize):
                curr=y+i
                if curr not in count:
                    return False
                count[curr]-=1
                if count[curr]==0:
                    del count[curr]
        return True