from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        q = deque()

        # 1. Find all treasures and add them to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))


        # 2. BFS
        while q:
            r, c = q.popleft()


            # 3. Explore four directions
            
            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
            #    - Check boundaries
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
            #    - Only visit INF cells
                elif grid[nr][nc] != INF:
                    continue
                else:
            #    - Update distance
                    grid[nr][nc] = grid[r][c] + 1
            #    - Add to queue
                    q.append((nr, nc))
    



