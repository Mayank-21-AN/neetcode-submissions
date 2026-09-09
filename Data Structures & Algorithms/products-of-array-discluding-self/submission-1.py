class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = []

        # Fill both lists with 1s
        pref = [1] * n
        suff = [1] * n

        # Build right products (from left to right)
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]
            

        # Build right products (from right t left)
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
            

        for i in range(n):
            result.append(pref[i] * suff[i])

        return (result)