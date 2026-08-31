class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_sets = [set() for _ in range(9)]
        row_sets = [set() for _ in range(9)]
        s_sets = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                # Calculate square idx
                s_id = int(3*(i // 3) + (j // 3))
                if board[i][j] == ".":
                    continue

                if board[i][j] in row_sets[i]:
                    return False
                else:
                    row_sets[i].add(board[i][j])
                    
                if board[i][j] in col_sets[j]:
                    return False
                else:
                    col_sets[j].add(board[i][j])

                if board[i][j] in s_sets[s_id]:
                    return False
                else:
                    s_sets[s_id].add(board[i][j])
        return True
