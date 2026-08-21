# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next

        curr=head
        ans=None
        prev_tail=None
        
        

        while length>=k:
            count=0
           
            prev=None
            start=curr
            while count<k:

                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
                count+=1
            if ans is  None:
                ans=prev
            if prev_tail:
                prev_tail.next=prev
            prev_tail=start
            length-=k

            
        prev_tail.next=curr
            


        return ans
            