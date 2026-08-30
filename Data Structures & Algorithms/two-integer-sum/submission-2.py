class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        sorted_indices = sorted(range(len(nums)), key=lambda i: nums[i])
        sorted_nums = [nums[i] for i in sorted_indices]
        while(i < j):
            if sorted_nums[i] + sorted_nums[j] > target:
                j = j - 1
            elif sorted_nums[i] + sorted_nums[j] < target:
                i = i + 1
            else:
                i = sorted_indices[i]
                j = sorted_indices[j]
                if i > j:
                    return [j, i]
                else:
                    return [i, j]


        