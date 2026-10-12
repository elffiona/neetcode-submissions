"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node):
            # 1. If already cloned, return the clone
            if node in old_to_new:
                return old_to_new[node]

            # 2. Create a new Node
            tmp = Node()
            tmp.val = node.val

            # 3. Store old-to-new mapping
            old_to_new[node] = tmp

            # 4. DFS through all neighbors
            #    and append their clones
            for n in node.neighbors:
                tmp.neighbors.append(dfs(n))

            # 5. Return the cloned node
            return tmp

        if not node:
            return None

        return dfs(node)
        