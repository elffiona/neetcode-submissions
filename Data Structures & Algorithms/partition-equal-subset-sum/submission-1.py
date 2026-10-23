class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # 1. Check whether total is odd
        if total % 2 == 1:
            return False

        target = total // 2

        # 2. Initialize Boolean DP
        dp = [False] * (target + 1)
        dp[0] = True

        # 3. Process each number
        for num in nums:
            # Update dp backwards
            for j in range(target, num - 1, -1):
            # dp[j] = dp[j] or dp[j - num]
                dp[j] = dp[j] or dp[j - num]

        # 4. Return answer
        return dp[target]