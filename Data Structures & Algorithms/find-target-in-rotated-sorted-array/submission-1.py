class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Find index of minimum element
        l = 0
        r = n - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                # Minimum is to the right of mid
                l = mid + 1
            else:
                # mid could itself be the minimum
                r = mid

        min_idx = l

        def bin_search(l, r):
            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return -1

        if min_idx == 0:
            return bin_search(0, n - 1)

        if nums[0] <= target <= nums[min_idx - 1]:
            return bin_search(0, min_idx - 1)
        else:
            return bin_search(min_idx, n - 1)

