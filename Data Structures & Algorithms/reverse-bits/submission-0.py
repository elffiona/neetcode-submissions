class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            # 1. Extract the last bit of n
            bit = n & 1 
            # 2. Shift result left and append the bit
            result = (result << 1) | bit
            # 3. Shift n right
            n = n >> 1

        return result