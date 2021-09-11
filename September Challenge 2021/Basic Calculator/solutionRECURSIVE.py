import operator


class Solution:
    def calculate(self, s: str) -> int:
        """Calculates an expression recursively"""
        def calculate_sub_term(term):
            res = 0
            idx = 0
            current = 0
            op = operator.add
            while idx < len(term):
                char = term[idx]
                if char.isdigit():
                    current = current * 10 + int(char)
                elif char == '+':
                    res = op(res, current)
                    current = 0
                    op = operator.add
                elif char == '-':
                    res = op(res, current)
                    current = 0
                    op = operator.sub
                elif char == '(':
                    current, offset = calculate_sub_term(term[idx + 1:])
                    idx += offset
                elif char == ')':
                    return op(res, current), idx + 1

                # always proceed (ignore whitespace)
                idx += 1

            return op(res, current), len(term)

        return calculate_sub_term(s)[0]
