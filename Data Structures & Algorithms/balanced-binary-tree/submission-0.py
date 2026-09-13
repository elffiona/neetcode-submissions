# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance_flag = True
        def dfs(r):
            nonlocal balance_flag
            if r is None:
                return 0
            else:
                left = dfs(r.left)
                right = dfs(r.right)
                if abs(left - right) > 1:
                    balance_flag = False
                return 1 + max(left, right)
        dfs(root)
        return balance_flag