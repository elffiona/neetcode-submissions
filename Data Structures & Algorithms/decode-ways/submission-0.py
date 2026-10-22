class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = 1

        if s[0] == "0":
            return 0

        dp[1] = 1

        for i in range(2, n + 1):
            c1 = 0
            c2 = 0

            # Last one digit
            if s[i - 1] != "0":
                c1 = dp[i - 1]

            # Last two digits
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                c2 = dp[i - 2]

            dp[i] = c1 + c2

        return dp[n]


         