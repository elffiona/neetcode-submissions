class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # dp[i][j]: whether s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        max_len = 1
        start = 0

        # 1. Base Case: Length = 1
        for i in range(n):
            # Every single character is a palindrome
            dp[i][i] = True

        # 2. Base Case: Length = 2
        for i in range(n - 1):
            # Check whether adjacent characters match
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                # Update max_len and start if necessary
                max_len = 2
                start = i

        # 3. DP: Length >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Check s[i] == s[j] and dp[i+1][j-1]
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                # If palindrome and longer than max_len,
                #       update max_len and start
                    if length > max_len:
                        max_len = length
                        start = i

        # 4. Return longest palindromic substring
        return s[start:start + max_len]