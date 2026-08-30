class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        result = [0] * len(nums)
        zero_cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                p *= nums[i]
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return result
        for i, c in enumerate(nums):
            if zero_cnt: result[i] = 0 if c else p
            else: result[i] = p // c
        return result
        