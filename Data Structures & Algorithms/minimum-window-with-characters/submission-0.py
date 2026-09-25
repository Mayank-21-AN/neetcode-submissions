class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Frequency map for target characters
        count_t= {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1    

        need = len(count_t)
        have = 0
        window = {}

        # Default makers before any valid window is found
        res = [-1,-1]
        min_len = float("inf")
        L = 0
        
        for R in range(len(s)):
            c = s[R]
            window[c] = window.get(c, 0) + 1

            if c in count_t and window[c] == count_t[c]:
                have += 1
            while have == need:
                if (R-L + 1) < min_len:
                    min_len = R - L + 1
                    res = [L, R]
                window[s[L]] -= 1
                if s[L] in count_t and window[s[L]] < count_t[s[L]]:
                    have -= 1   
                L += 1
        L_ans, R_ans = res[0], res[1]

        if min_len != float("inf"):
            return s[L_ans: R_ans + 1]
        else:
            return ""
        