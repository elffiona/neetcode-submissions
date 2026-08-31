class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p_i = 0
        p_j = len(s) - 1
        while p_i != p_j and p_i < len(s) and p_j > 0:
            if not s[p_i].isalnum():
                p_i += 1
                continue

            if not s[p_j].isalnum():
                p_j -= 1
                continue
            
            if s[p_i] == s[p_j]:
                p_i += 1
                p_j -= 1
            else:
                return False
        return True


        