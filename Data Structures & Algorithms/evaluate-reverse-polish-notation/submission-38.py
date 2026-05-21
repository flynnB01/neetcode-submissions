from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in '+-*/':
                num2 = stack.pop()
                num1 = stack.pop()
                
                if c == '+':
                    stack.append(int(num1) + int(num2))
                elif c == '-':
                    stack.append(int(num1) - int(num2))
                elif c == '*':
                    stack.append(int(num1) * int(num2))
                else:
                    division = int(num1) / int(num2)
                    if division > 0:
                        stack.append(floor(division))
                    else:
                        stack.append(ceil(division))
            else:
                stack.append(c)

        return int(stack.pop())