class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                # Check if coin <= i
                if coin <= i:
                    diff = i - coin
                    # Update dp[i]
                    dp[i] = min(dp[i], 1 + dp[diff])

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
