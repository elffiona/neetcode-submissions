# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def re_helper(head):
            prev = None
            curr = head
            while curr:
                n = curr.next
                curr.next = prev
                prev = curr
                curr = n
            return prev
        
        p_t = None
        t = head
        for i in range(k):
            if t:
                p_t = t
                t = t.next
            else:
                # Less than k
                return head
        # At this point t is the start of the remaining
        # p_t is the tail
        # Break between p_t and t
        p_t.next = None
        # Reverse first k
        dd = re_helper(head)
        # Now head is the tail
        head.next = self.reverseKGroup(t, k)
        return dd
        
    

                
        