class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        substr = set()

        for right in range(len(s)):
            # add nums[right] into the window
            while s[right] in substr:
                substr.remove(s[left])
                left += 1
            
            substr.add(s[right])
            result = max(result, len(substr))
        
        return result