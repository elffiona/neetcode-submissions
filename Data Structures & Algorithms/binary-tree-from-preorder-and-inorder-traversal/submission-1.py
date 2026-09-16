# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        preorder_idx = 0

        def dfs(left, right):
            nonlocal preorder_idx

            if left > right:
                return None

            # preorder 中下一个一定是当前 subtree 的 root
            root_val = preorder[preorder_idx]
            preorder_idx += 1

            root = TreeNode(root_val)

            # root 在 inorder 中的位置
            mid = inorder_idx[root_val]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)
        