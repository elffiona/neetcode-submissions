class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, min(i, n) + 1):
                # Check s[i - 1] and t[j - 1]
                if s[i - 1] == t[j - 1]:
                    # Can take or skip
                    # Take: s[:i-2] need to be t[:j-2]
                    # Skip: s[:i-2] need to be t[:j-1]
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # Has to skip
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]