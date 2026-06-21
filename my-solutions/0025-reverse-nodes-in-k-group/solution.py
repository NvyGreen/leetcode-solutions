# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev_sec = None
        new_head = None

        try:
            while fast is not None:
                for i in range(k):
                   fast = fast.next
                
                sec_head, sec_tail = self.reverseLengthK(slow, k)
                if prev_sec is not None:
                    prev_sec.next = sec_head
                if new_head is None:
                    new_head = sec_head
                
                sec_tail.next = fast
                prev_sec = sec_tail
                slow = fast
        except AttributeError:
            pass

        return new_head if new_head is not None else head
    

    def reverseLengthK(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = head
        prev = None
        curr = head

        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev, tail
