class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + tmp
            tmp = digits[i] // 10
            digits[i] = digits[i] % 10

        # Deal with the first one
        if tmp == 1:
            digits = [1] + digits
        
        return digits
                

