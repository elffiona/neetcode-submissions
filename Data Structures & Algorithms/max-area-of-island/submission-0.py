class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        m_area = 0

        def dfs(r, c):
            # TODO 1: Boundary check
            if r >= rows or c >= cols or r < 0 or c < 0:
                return 0

            # TODO 2: Check whether current cell is water
            if grid[r][c] == 0:
                return 0

            # TODO 3: Mark current cell as visited
            grid[r][c] = 0
            
            # TODO 4: Explore four directions
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # TODO 5: Found a new island
                    area = dfs(r, c)
                    if m_area < area:
                        m_area = area

        return m_area