class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)

        if len(dp) > 1:
            dp[1] = cost[0]

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 2], dp[i - 1])
            dp[i] += cost[i - 1]

        dp[-1] = dp[-3]

        
        return min(dp[-1], dp[-2])