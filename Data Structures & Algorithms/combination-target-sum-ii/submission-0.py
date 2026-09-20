class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()

        def backtrack(start, remain):
            if remain == 0:
                result.append(path[:])
            # Still remaining
            for i in range(start, len(candidates)):
                # Skip if I have used this number once at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    # Can't add this
                    continue
                # Add this
                path.append(candidates[i])
                # Check if we want to add this again
                backtrack(i + 1, remain - candidates[i])
                path.pop()

        backtrack(0, target)
        return result