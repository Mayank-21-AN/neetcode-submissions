class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        basket = {}
        result = []
        for num in nums:
            basket[num] = basket.get(num, 0) + 1

        boxes = [[] for _ in range(len(nums) + 1)]

        for num,count in basket.items():
            boxes[count].append(num)

        for bucket in reversed(boxes):
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return (result)
