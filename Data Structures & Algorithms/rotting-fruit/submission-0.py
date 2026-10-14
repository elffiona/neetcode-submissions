class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        minutes = 0
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # Append all rotten fruit
                    q.append((r, c))
                elif grid[r][c] == 1:
                    # Note down all fresh
                    fresh_count += 1
        
        while q and fresh_count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                # Explore neighbors
                directions = [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1)
                ]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nc < 0 or nr < 0 or nc >= cols or nr >= rows:
                        continue
                    elif grid[nr][nc] != 1:
                        continue
                    else:
                        # Fresh!
                        # Infect fresh fruit
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        # fresh -= 1
                        fresh_count -= 1

            minutes += 1

        return minutes if fresh_count == 0 else -1

                
        


        