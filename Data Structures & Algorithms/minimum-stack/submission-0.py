class MinStack:

    def __init__(self):
        # min_stack mirrors stack to track the minimum value at every state of O(1)
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.min_stack == []:
            self.min_stack.append(val)
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)
        self.stack.append(val)
        
    def pop(self) -> None:
        # Keep both stacks synchronized so historical minimums are restored
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        

        

