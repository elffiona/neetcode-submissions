class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_stack = []
        left_bar = [-1]*n
        for i in range(n):
            while left_stack and heights[left_stack[-1]] >= heights[i]:
                left_stack.pop()
            if left_stack:
                left_bar[i] = left_stack[-1]
            left_stack.append(i)
        
        right_stack = []
        right_bar = [n]*n
        for i in range(n - 1, -1, -1):
            while right_stack and heights[right_stack[-1]] >= heights[i]:
                right_stack.pop()
            if right_stack:
                right_bar[i] = right_stack[-1]
            right_stack.append(i)

        # Now compute area
        max_a = 0
        for i in range(n):
            left_bar[i] += 1
            right_bar[i] -= 1
            max_a = max(max_a, heights[i]*(right_bar[i] - left_bar[i] + 1))
        return max_a
