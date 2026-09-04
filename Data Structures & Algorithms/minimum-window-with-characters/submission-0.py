class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # Build frequency map for t
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        window = {}
        have = 0
        need_count = len(need)

        result = [-1, -1]
        result_len = float("inf")

        left = 0

        for right in range(len(s)):
            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            # Did we just satisfy one requirement?
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Current window contains everything we need
            # Window is valid
            while have == need_count:

                # Update minimum window
                if right - left + 1 < result_len:
                    result = [left, right]
                    result_len = right - left + 1

                # Remove s[left]
                left_char = s[left]
                window[left_char] -= 1

                # Did removing this character break a requirement?
                if (
                    left_char in need
                    and window[left_char] < need[left_char]
                ):
                    have -= 1

                left += 1

        l, r = result

        return s[l:r + 1] if result_len != float("inf") else ""
