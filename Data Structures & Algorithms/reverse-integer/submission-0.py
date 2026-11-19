class Solution:
    def reverse(self, x: int) -> int:
        # 1. Save the sign
        sign = 1 if x >= 0 else -1

        # 2. Work with the absolute value
        x = abs(x)
        rev = 0

        # 3. Reverse the digits
        while x > 0:
            # Extract the last digit
            digit = x % 10

            # Append digit to rev
            rev = rev * 10 + digit

            # Remove the last digit from x
            x = x // 10

        # 4. Restore the sign
        rev = rev * sign

        # 5. Check 32-bit signed integer range
        if rev < -(2 ** 31) or rev > 2 ** 31 - 1:
            return 0

        return rev