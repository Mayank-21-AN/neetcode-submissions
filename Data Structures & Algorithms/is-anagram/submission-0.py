class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_text_1 = "".join(sorted(s))
        sorted_text_2 = "".join(sorted(t))

        if len(s) == len(t):
            if sorted_text_1 == sorted_text_2:
                return True
        return False