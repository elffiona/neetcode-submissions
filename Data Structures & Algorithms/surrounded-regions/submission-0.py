class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            # Already visited?
            if board[r][c] == "#":
                return

            # is O?
            if board[r][c] != "O":
                return

            # Mark visited
            board[r][c] = "#"
            

            # Explore four directions
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
                else:
            #    - DFS neighbor
                    dfs(nr, nc)

        # Start DFS from boundaries
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)

        # Scan for "O"
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

        