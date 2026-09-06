class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_helper(l, r, nums, target):
            if l > r:
                return -1
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                # Search right
                return binary_helper(m + 1, r, nums, target)
            else:
                # Search left
                return binary_helper(l, m - 1, nums, target)

        return binary_helper(0, len(nums) - 1, nums, target)


        