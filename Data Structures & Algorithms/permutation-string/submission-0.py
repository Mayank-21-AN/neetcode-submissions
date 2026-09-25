class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        s2_count = {}
        L = 0
        for R in range(len(s2)):
            s2_count[s2[R]] = s2_count.get(s2[R], 0) + 1

            if (R - L + 1) > len(s1):
                s2_count[s2[L]] -= 1
                if s2_count[s2[L]] == 0:
                    del s2_count[s2[L]]
                L += 1

            if s1_count == s2_count:
                return True

        return False