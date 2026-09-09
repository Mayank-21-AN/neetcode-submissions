class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_len = 0
        for i in nums: # Loop through unique numbers to check each as a potential sequence start
            x = 1
            if (i-1) not in num_set: 
                while (i + x) in num_set: # Update max_len if the current streak (x) is the longest seen so far
                    x += 1
                max_len = max(max_len,x)
        return max_len