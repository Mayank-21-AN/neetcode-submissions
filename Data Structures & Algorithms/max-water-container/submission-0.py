class Solution:
    def maxArea(self, heights: List[int]) -> int:
                
        L = 0
        R = len(heights) - 1
        max_area = 0

        while L < R:
            # 1. Calculate the current area first
            Current_area = (R-L)* min(heights[L],heights[R])

            # 2. Update max_area
            max_area = max(max_area,Current_area)

            # 3. Move the pointer of the Shorter wall
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return max_area