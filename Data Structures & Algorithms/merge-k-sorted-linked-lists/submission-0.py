# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwo(l1, l2):
            dummy = ListNode(0)
            tail = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next

                tail = tail.next

            tail.next = l1 if l1 else l2
            return dummy.next
        
        def mergeRange(left, right):
            if left > right:
                return None

            if left == right:
                return lists[left]

            mid = left + (right - left) // 2

            l1 = mergeRange(left, mid)
            l2 = mergeRange(mid + 1, right)

            return mergeTwo(l1, l2)
            
        return mergeRange(0, len(lists) - 1)
        

        