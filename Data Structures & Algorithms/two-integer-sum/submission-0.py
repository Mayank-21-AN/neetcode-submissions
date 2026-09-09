class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        basket = {}
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in basket:
                final = basket[diff],index
                return (list(final))
            else:
                basket[num] = index
                
