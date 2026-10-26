class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(prices))]

        # 0 hold 1 sell 2 ready

        dp[0][0] = -prices[0]
        dp[0][1] = float('-inf')

        for i in range(1, len(prices)):
            # Hold
            # hold yesterday or ready yesterday and buy today
            dp[i][0] = max(dp[i - 1][2] - prices[i], dp[i-1][0])
            # Sell
            # hold yesterday
            dp[i][1] = dp[i - 1][0] + prices[i]
            # Ready
            # ready yesterday or sell yesterday
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])

        return max(dp[-1][1], dp[-1][2])
