class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        q = self.reverseList(slow.next)
        slow.next = None
        p = head

        while p and q:
            p_next = p.next
            q_next = q.next
            p.next = q
            q.next = p_next
            p = p_next
            q = q_next

    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
