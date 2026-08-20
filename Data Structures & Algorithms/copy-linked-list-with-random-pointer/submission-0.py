"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new={}
        curr=head
        while curr:
            old_new[curr]=Node(curr.val)
            curr=curr.next

        curr=head
        while curr:
            curr2=old_new[curr]
            curr2.random=old_new[curr.random] if curr.random else None
            curr2.next=old_new[curr.next] if curr.next else None
            curr=curr.next
        return old_new[head] if head else None
        