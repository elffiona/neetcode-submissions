class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            # TODO 1: Boundary check
            if r >= rows or c >= cols or r < 0 or c < 0:
                return

            # TODO 2: Check whether current cell is water
            if grid[r][c] == "1":

            # TODO 3: Mark current cell as visited
                grid[r][c] = "0"
            else:
                return

            # TODO 4: Explore four directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # TODO 5: Found a new island
                    count += 1
                    dfs(r, c)

        return count