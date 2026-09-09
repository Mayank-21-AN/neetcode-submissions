class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        basket = {}

        for num in nums:
            basket[num] = basket.get(num, 0) + 1
        count = sorted(basket.items(), reverse= True, key= lambda x: x[1])
        result = [num for num, count in count[:k]]

        return result
