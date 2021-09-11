class Solution:
    def calculate(self, s: str) -> int:
        """Calculates an expression using a stack"""
        res = 0
        stack = []
        current = 0
        sign = 1
        for char in s:
            if char.isdigit():
                current = current * 10 + int(char)
            elif char == '+':
                res += current * sign
                current = 0
                sign = 1
            elif char == '-':
                res += current * sign
                current = 0
                sign = -1
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ')':
                res += current * sign
                current = 0
                res *= stack.pop()  # sign
                res += stack.pop()  # old res

        return res + current * sign
