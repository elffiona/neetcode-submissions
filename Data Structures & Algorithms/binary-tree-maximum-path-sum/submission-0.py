# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Maximum gain we can get from left/right child.
            # If negative, don't take that branch.
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Complete path with current node as the highest point
            current_path = node.val + left + right
            self.maximum = max(self.maximum, current_path)

            # Return only ONE branch to parent
            return node.val + max(left, right)

        dfs(root)
        return self.maximum