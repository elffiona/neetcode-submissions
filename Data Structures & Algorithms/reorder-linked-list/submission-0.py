# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reorder_helper(h, t):
            # Already at tail
            if t is None:
                return h

            # Recursively move t toward the tail
            h = reorder_helper(h, t.next)

            # Reordering already finished
            if h is None:
                return None

            # Front and back meet/cross
            if h == t or h.next == t:
                t.next = None
                return None

            # Insert t after h
            tmp = h.next
            h.next = t
            t.next = tmp

            # Move front pointer forward
            return tmp

        reorder_helper(head, head.next)