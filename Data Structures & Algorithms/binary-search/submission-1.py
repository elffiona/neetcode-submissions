class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left <= right:
            ind = (left + right) // 2
            if (nums[ind] == target):
                return ind
            elif (nums[ind] < target):
                left = ind + 1
            else:
                right = ind - 1
        return -1


        