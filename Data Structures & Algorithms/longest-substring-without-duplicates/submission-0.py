class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        R = 0

        max_len = 0
        char_set = set()

        for R in range(len(s)):
            # Shrink window from left until duplicate is gone
            while s[R] in char_set:
                char_set.remove(s[L]) # Evict left character
                L += 1 # Move left edge inward

            char_set.add(s[R])
            # +1 counts both ends inclusive (window size)
            max_len = max(max_len, R - L + 1) 

        return (max_len)
