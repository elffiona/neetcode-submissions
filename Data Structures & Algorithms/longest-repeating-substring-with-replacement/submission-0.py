class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        count = {}
        max_freq = 0

        for right in range(len(s)):
            # Add s[right] into the window
            count[s[right]] = count.get(s[right], 0) + 1

            # Frequency of the most common character in the window
            max_freq = max(max_freq, count[s[right]])

            # Number of replacements needed:
            # window size - most frequent char count
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
        