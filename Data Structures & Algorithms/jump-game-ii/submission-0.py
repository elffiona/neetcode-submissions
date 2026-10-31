class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        end = 0
        jump_steps = 0

        for i in range(len(nums) - 1):
            # Update far
            n = i + nums[i]
            if i <= far and n > far:
                far = n
            # If i == end, complete current jump
            if i == end:
                jump_steps += 1
                end = far

        return jump_steps