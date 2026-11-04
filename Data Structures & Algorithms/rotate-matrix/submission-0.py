class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 1. Process each layer
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer

            # 2. Traverse the top edge
            for i in range(first, last):

                # Four positions
                top = (first, i)
                right = (i, last)
                bottom = (last, n - 1 - i)
                left = (n - 1 - i, first)

                # 3. Perform 4-way swap
                # top -> right -> bottom -> left -> top

                tmp = matrix[top[0]][top[1]]
                matrix[top[0]][top[1]] = matrix[left[0]][left[1]]
                matrix[left[0]][left[1]] = matrix[bottom[0]][bottom[1]]
                matrix[bottom[0]][bottom[1]] = matrix[right[0]][right[1]]
                matrix[right[0]][right[1]] = tmp
        