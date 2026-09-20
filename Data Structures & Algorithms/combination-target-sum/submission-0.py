class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start, remain):
            if remain == 0:
                result.append(path[:])
                return
            
            # Still remaining
            for i in range(start, len(nums)):
                if nums[i] > remain:
                    # Can't add this
                    continue
                # Add this
                path.append(nums[i])
                # Check if we want to add this again
                backtrack(i, remain - nums[i])
                path.pop()

        backtrack(0, target)
        return result