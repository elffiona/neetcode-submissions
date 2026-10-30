class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j]: whether s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 1. Base case
        dp[0][0] = True

        # 2. Empty string vs pattern
        for j in range(2, n + 1):
            if p[j - 1] == "*":
                # TODO: Zero occurrences
                dp[0][j] = dp[0][j - 2]

        # 3. Fill DP
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if p[j - 1] != "*":
                    # TODO: Normal character or '.'
                    if p[j - 1] == "." or s[i - 1] == p[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
                else:
                    # TODO 1: '*' matches zero characters
                    # meaning we look at whether the pattern before * and its preceding char can match s
                    case1 = dp[i][j - 2]

                    # TODO 2: '*' matches one or more
                    # Check whether p[j-2] matches s[i-1]
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        case2 = dp[i - 1][j]
                    else:
                        case2 = False
                    
                    dp[i][j] = case1 or case2

        # 4. Return result
        return dp[m][n]