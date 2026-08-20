class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr = ans
        carry = 0

        while l1 or l2:
            x = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            value = x % 10
            carry = x // 10

            curr.val = value

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 or l2 or carry:
                curr.next = ListNode()
                curr = curr.next

        if carry:
            curr.val = carry

        return ans