class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        L = 0
        count = {}
        max_len = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            # Only shrink from left IF we need more replacements than budget k
            while (R - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1
            # Once the loop finishes, window is guarenteed to be valid!
            max_len = max(max_len, R - L + 1)

        return (max_len)