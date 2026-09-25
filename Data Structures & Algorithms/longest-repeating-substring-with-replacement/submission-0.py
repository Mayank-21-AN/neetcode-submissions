class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        max_len = 0

        for R in range(len(s)):
            # 1. Add current character to tally
            count[s[R]] = 1 + count.get(s[R], 0)

            # 2. While outsiders to replace > k, shrink from left
            while (R - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1

            # 3. Window is valid, update maximum length
            max_len = max(max_len, R - L + 1)

        return max_len