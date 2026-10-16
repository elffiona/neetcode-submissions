class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            # 1. Find root of u
            root_u = find(u)
            # 2. Find root of v
            root_v = find(v)
            # 3. If roots are equal, return False
            if root_u == root_v:
                return False
            # 4. Otherwise, merge the two components
            else:
                parent[root_u] = root_v
            # 5. Return True
                return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        