class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # dp[i][j]: whether s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        count = 0

        # 1. Base Case: Length = 1
        for i in range(n):
            # Every single character is a palindrome
            dp[i][i] = True
            count += 1

        # 2. Base Case: Length = 2
        for i in range(n - 1):
            # Check whether adjacent characters match
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1

        # 3. DP: Length >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Check s[i] == s[j] and dp[i+1][j-1]
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1

        # 4. Return number of palindromic substrings
        return count