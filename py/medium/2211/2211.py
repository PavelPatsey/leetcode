class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        stack = []
        for d in directions:
            if d == "R":
                stack.append(d)
            elif d == "S":
                res += count_right(stack)
                stack = ["S"]
            else:
                if stack and stack[-1] in {"S", "R"}:
                    res += count_right(stack) + 1
                    stack = ["S"]
                else:
                    stack.append(d)
        return res


def count_right(stack: list[int]) -> int:
    counter = 0
    i = len(stack) - 1
    while i >= 0 and stack[i] == "R":
        counter += 1
        i -= 1
    return counter


solution = Solution()
assert solution.countCollisions("RLRSLL") == 5
assert solution.countCollisions("LLRR") == 0
