class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0

        for i in range(len(nums)):
            # Jump!
            j = nums[i]
            n = j + i

            if i <= far and n > far:
                far = n
        
        return len(nums) - 1 <= far