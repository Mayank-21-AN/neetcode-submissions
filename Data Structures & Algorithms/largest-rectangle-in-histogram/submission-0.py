class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (start_index, height)

        for i, h in enumerate(heights):
            start = i
            # Pop taller bars because current bar blocks them
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index  # Extend current bar backwards
            stack.append((start, h))

        # Bars that reached the right boundary
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
        
        return max_area
