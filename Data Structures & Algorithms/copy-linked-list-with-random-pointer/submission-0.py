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
        mm = {}
        def copy_helper(h):
            if h is None:
                return None

            if h in mm:
                return mm[h]
            
            copy = Node(h.val)
            mm[h] = copy
            copy.next = copy_helper(h.next)
            copy.random = mm.get(h.random)

            return copy

        return copy_helper(head)