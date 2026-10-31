class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = -float('inf')
        curr = 0
        for n in nums:
            curr += n
            best = max(curr, best)
            if curr < 0:
                curr = 0
        
        return best