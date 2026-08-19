# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow, fast = head, head
        while fast is not None:
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
            slow = slow.next
            if slow == fast:
                return True
        
        return False
