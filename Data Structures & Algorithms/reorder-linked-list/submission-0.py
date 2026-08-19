# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # 1. Find length
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        # 2. Find start of second half
        mid = (length + 1) // 2

        curr = head
        prev = None

        for i in range(mid):
            prev = curr
            curr = curr.next

        # Separate the two halves
        prev.next = None

        # 3. Reverse second half
        reversed_prev = None

        while curr:
            nxt = curr.next
            curr.next = reversed_prev
            reversed_prev = curr
            curr = nxt

        # 4. Merge the two halves
        first = head
        second = reversed_prev

        while first and second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next