# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False
        else:
            ll = self.isSameTree(p.left, q.left)
            rr = self.isSameTree(p.right, q.right)
            if ll and rr:
                return p.val == q.val
            else:
                return False