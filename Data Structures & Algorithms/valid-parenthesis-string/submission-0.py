class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for c in s:
            if c == "(":
                low += 1
                high += 1
            elif c == "*":
                # Think of it as ")"
                low = max(0, low - 1)
                # Think of it as "("
                high += 1
            else:
                # c = )
                low = max(0, low - 1)
                high -= 1
                if high < 0:
                    return False

        return low == 0