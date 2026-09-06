class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_0 = [row[0] for row in matrix]
        l = 0
        r = len(col_0) - 1
        row_idx = -1
        # Find the last row whose first element <= target
        while l <= r:
            mid = l + (r - l) // 2

            if col_0[mid] <= target:
                row_idx = mid
                l = mid + 1
            else:
                r = mid - 1

        if row_idx == -1:
            return False

        row_l = matrix[row_idx]
        l = 0
        r = len(row_l) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if row_l[mid] == target:
                return True
            elif row_l[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        # If did not return, not found
        return False
        