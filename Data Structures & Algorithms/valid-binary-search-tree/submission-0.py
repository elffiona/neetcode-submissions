# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, float('inf'), float('-inf')

            left_valid, left_min, left_max = dfs(node.left)
            right_valid, right_min, right_max = dfs(node.right)

            if (
                not left_valid
                or not right_valid
                or left_max >= node.val
                or right_min <= node.val
            ):
                return False, 0, 0

            subtree_min = min(left_min, node.val)
            subtree_max = max(right_max, node.val)

            return True, subtree_min, subtree_max

        return dfs(root)[0]