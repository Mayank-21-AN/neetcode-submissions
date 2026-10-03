class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        output = []
        q = deque()
        L = 0

        for R in range(len(nums)):
            #1. Back Kick: If new number is greater than the previously added number, pop it from back
            while q and nums[R] > nums[q[-1]]:
                q.pop()
            q.append(R)

            #2. Front Kick: If front index is behind the boundary L, pop it from left because it expired
            if q[0] < L:
                q.popleft()
                
            #3. Save & Slide: Once window size reaches k, append front max to output and move L forward
            if (R + 1) >= k:
                output.append(nums[q[0]])
                L += 1
        return output