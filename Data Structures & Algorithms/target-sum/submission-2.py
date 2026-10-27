class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            new_dp = {}

            for s, count in dp.items():
                # TODO: Add num
                # TODO: Subtract num
                # Remember to accumulate counts!
                if s - num not in new_dp:
                    new_dp[s - num] = 0
                if s + num not in new_dp:
                    new_dp[s + num] = 0

                new_dp[s - num] += count
                new_dp[s + num] += count

            dp = new_dp

        return dp.get(target, 0)