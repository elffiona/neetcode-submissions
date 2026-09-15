# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        final_list = {}
        
        def dfs(node, depth):
            if not node:
                return None
            if depth not in final_list:
                final_list[depth] = 0
            
            final_list[depth] = max(final_list[depth], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)

        result = []
        for key, value in final_list.items():
            result.append(value)
        return result

        
        