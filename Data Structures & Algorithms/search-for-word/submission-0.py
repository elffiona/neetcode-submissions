class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, i):
            # word done
            if i == len(word):
                return True
            # Invalid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if board[r][c] != word[i]:
                return False

            # Match word[i]!
            temp = board[r][c]
            # Used
            board[r][c] = "#"
            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )

            # Backtrack
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False
