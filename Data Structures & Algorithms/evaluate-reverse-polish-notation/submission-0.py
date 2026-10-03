class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for  token in tokens:
            match token:
                case "+":
                    # Pop right operand first, then left operand
                    b, a = stack.pop(), stack.pop()
                    stack.append(a + b)
                case "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                case "*":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a * b)
                case "/":
                    # int() truncates float division toward zero as required
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
                case _:
                    # Push numerical operands directly as integers
                    stack.append(int(token))
        
        return stack[0]