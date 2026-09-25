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
            # Expand window to the right
            c = s[R]
            window[c] = window.get(c, 0) + 1

            # Check if current character satisfies required count 
            if c in count_t and window[c] == count_t[c]:
                have += 1
            # Shrink window form left to find minimum length
            while have == need:
                # Save smallest window seen so far
                if (R-L + 1) < min_len:
                    min_len = R - L + 1
                    res = [L, R]
                # Evict left character and check if quota was broken 
                window[s[L]] -= 1
                if s[L] in count_t and window[s[L]] < count_t[s[L]]:
                    have -= 1   
                L += 1
        # Return minimum substring if found, else empty string
        L_ans, R_ans = res[0], res[1]
    
        if min_len != float("inf"):
            return s[L_ans: R_ans + 1]
        else:
            return ""
        