class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and stack[-1][0] < t:
                idx = stack[-1][1]
                result[idx] = i - idx
                stack.pop()

            stack.append((t, i))
        return result
                
        