class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1 
            R = len(nums) - 1
            while L < R:
                current_sum = nums[i] + nums[L] + nums[R]

                if current_sum < 0:
                    L += 1         
                elif current_sum > 0:
                    R -= 1
                else:
                    res.append(list((nums[i],nums[L],nums[R])))
                    L += 1
                    # Skip any adjacent duplicates of the left pointer
            # Keep moving L forward if the next number is identical
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        return res