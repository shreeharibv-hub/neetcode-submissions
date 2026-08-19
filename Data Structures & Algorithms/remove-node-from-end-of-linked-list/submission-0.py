# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        m=length-n
           # Special case: remove head
        if m == 0:
            return head.next

        pos=1
        curr=head
        
        while curr and curr.next:
            if pos==m:
                curr.next=curr.next.next
            pos+=1
    
            curr=curr.next
        return head
       

        
        