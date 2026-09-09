class Solution:
    def isPalindrome(self, s: str) -> bool:
        given_s = ""

        for i in s.lower():
            if i.isalnum(): # it only checks for Alphabets and numbers only
                given_s += i

        return given_s == given_s[::-1] # it checks the main string with reverse of it.
            