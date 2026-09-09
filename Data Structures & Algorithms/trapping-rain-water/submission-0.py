class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        max_water = 0
        left_max = height[L]
        right_max = height[R]
        while L < R:

            if left_max < right_max:
                L += 1
                left_max = max(left_max, height[L])
                max_water += left_max - height[L]
            else:
                R -= 1
                right_max = max(right_max, height[R])
                max_water += right_max - height[R]

        return max_water