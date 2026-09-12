# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        elif root.left is None and root.right is None:
            # Leaf
            return root
        else:
            # Revert recursively
            r = root.right
            root.right = self.invertTree(root.left)
            root.left = self.invertTree(r)
        return root
            
        