import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]

        heap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            time, r, c = heapq.heappop(heap)

            # 1. Skip outdated entries
            if time > dist[r][c]:
                continue

            # 2. If reached destination, return time
            if r == n - 1 and c == n - 1:
                return time

            # 3. Explore four directions
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
            #    - Check boundaries
                if nr < 0 or nc < 0 or nr > n - 1 or nc > n - 1:
                    continue
            #    - Calculate new_time using max()
                new_time = max(dist[r][c], grid[nr][nc])
            #    - Relax and push to heap
                if new_time < dist[nr][nc]:
                    dist[nr][nc] = new_time
                    heapq.heappush(heap, (new_time, nr, nc))
        