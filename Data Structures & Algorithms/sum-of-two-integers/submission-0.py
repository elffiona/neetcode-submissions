class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        while b:
            # Calculate sum without carry
            s = (a ^ b) & MASK
            # Calculate carry
            c = ((a & b) << 1) & MASK
            # Update a and b
            a = s
            b = c

        if a > 0x7FFFFFFF:
            return a - (1 << 32)
        return a