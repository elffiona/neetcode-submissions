class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]

        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]

            dp[r][c] = 1
            directions = [
                (1, 0),   # Down
                (-1, 0),  # Up
                (0, 1),   # Right
                (0, -1)   # Left
            ]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                # Check matrix[nr][nc] > matrix[r][c]
                if matrix[nr][nc] > matrix[r][c]:
                    dp[r][c] = max(dp[r][c], 1 + dfs(nr, nc))

            return dp[r][c]

        for i in range(rows):
            for j in range(cols):
                dp[i][j] = dfs(i, j)

        return max(max(row) for row in dp)