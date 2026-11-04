class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        result = []

        # 1. Initialize boundaries
        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        # 2. Spiral traversal
        while top <= bottom and left <= right:

            # Right: traverse top row
            # TODO: from left to right
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # Down: traverse right column
            # TODO: from top to bottom
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # Left: traverse bottom row
            if top <= bottom:
                # TODO: from right to left
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            # Up: traverse left column
            if left <= right:
                # TODO: from bottom to top
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result