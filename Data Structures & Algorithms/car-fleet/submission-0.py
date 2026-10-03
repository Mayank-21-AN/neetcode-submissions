class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed; sort from closest to target to farthest
        cars = sorted(zip(position, speed), reverse= True)
        stack = [] # Stores the arrival time of each distinct fleet leader

        for p, s in cars:
            time = (target - p) / s
            stack.append(time)

            # If current car reaches target at or before the car ahead,
            # it catches up and merges into that fleet (pop the trailing car)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

   
        