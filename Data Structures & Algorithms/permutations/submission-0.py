class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                # Check if this is used in current path
                if used[i]:
                    continue
                
                # Have not been used
                path.append(nums[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
        
        backtrack()
        return result
        