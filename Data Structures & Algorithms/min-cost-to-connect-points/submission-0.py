class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                # Calculate Manhattan Distance
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                # Append (cost, i, j)
                edges.append((cost, i, j))

        edges.sort()

        parent = list(range(n))

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
        
        total_cost = 0
        edges_used = 0

        for cost, u, v in edges:
            if union(u, v):
                total_cost += cost
                edges_used += 1

                if edges_used == n - 1:
                    break
        return total_cost