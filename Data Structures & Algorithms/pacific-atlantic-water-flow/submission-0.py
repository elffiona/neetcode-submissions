class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            # 1. Already visited?
            if (r, c) in visited:
                return

            # 2. Mark visited
            visited.add((r, c))

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
                if nc < 0 or nr < 0 or nc >= cols or nr >= rows:
                    continue
            #    - Check height >= current height
                elif heights[nr][nc] < heights[r][c]:
                    continue
                else:
            #    - DFS neighbor
                    dfs(nr, nc, visited)

        # 4. Start DFS from Pacific boundaries
        # 5. Start DFS from Atlantic boundaries
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols - 1, atlantic)
        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows - 1, j, atlantic)

        # 6. Find intersection
        return [[r, c] for r, c in pacific & atlantic]
        