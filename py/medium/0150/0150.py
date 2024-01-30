from typing import List


class Solution:
    OPERATORS = {
        "+": lambda x, y: y + x,
        "-": lambda x, y: y - x,
        "*": lambda x, y: y * x,
        "/": lambda x, y: int(y / x),
    }

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in self.OPERATORS:
                operator = self.OPERATORS[token]
                stack.append(operator(stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        return stack[0]


solution = Solution()
assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert (
    solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
    == 22
)
