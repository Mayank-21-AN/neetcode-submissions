class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize result with 0s; days that never find a warmer day remain 0
        result = [0] * len(temperatures)
        stack = [] # Monotonic decreasing stack storing only indices
            
        for i, current_temp in enumerate(temperatures):
                # Resolve all earlier colder days waiting in the stack
                while stack and current_temp > temperatures[stack[-1]]:
                    prev_i  = stack.pop()
                    result[prev_i] = i - prev_i
                # Add today's index to the stack to wait for a warmer day
                stack.append(i)
        return result