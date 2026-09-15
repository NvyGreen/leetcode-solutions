# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p, q = headA, headB
        visited = set()

        while p and q:
            if p == q or p in visited:
                return p
            if q in visited:
                return q
            
            visited.add(p)
            visited.add(q)
            p = p.next
            q = q.next
        
        while p:
            if p in visited:
                return p
            # visited.add(p)
            p = p.next
        
        while q:
            if q in visited:
                return q
            # visited.add(q)
            q = q.next
        
        return None
