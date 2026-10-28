class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        # 1. Add virtual balloons
        nums = [1] + nums + [1]

        # 2. Initialize DP
        # dp[i][j]: max coins from bursting
        # all balloons in interval [i, j]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # 3. Iterate by interval length
        for length in range(1, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1

                # 4. Try every balloon as the LAST one
                for k in range(i, j + 1):

                    # TODO 1: Max coins from left interval
                    left = dp[i][k - 1]

                    # TODO 2: Max coins from right interval
                    right = dp[k + 1][j]

                    # TODO 3: Coins from bursting k last
                    coins = nums[i - 1]*nums[k]*nums[j + 1]

                    # TODO 4: Update dp[i][j]
                    dp[i][j] = max(dp[i][j], left+right+coins)

        # 5. Return max coins for all real balloons
        return dp[1][n]
        