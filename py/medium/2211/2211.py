class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        stack = []
        for d in directions:
            if d == "R":
                if stack and stack[-1] in {"L", "S"}:
                    stack = []
                stack.append(d)
            elif d == "S":
                if stack and stack[-1] in {"L", "S"}:
                    stack = ["S"]
                else:
                    counter = 0
                    while stack and stack[-1] == "R":
                        stack.pop()
                        counter += 1
                    res += counter
                    stack = ["S"]
            elif d == "L":
                if stack and stack[-1] == "S":
                    res += 1
                    stack = ["S"]
                elif stack and stack[-1] == "R":
                    counter = 0
                    while stack and stack[-1] == "R":
                        stack.pop()
                        counter += 1
                    res += counter
                    res += 1
                    stack = ["S"]
                else:
                    stack.append("L")
            else:
                assert False
        return res


solution = Solution()
assert solution.countCollisions("RLRSLL") == 5
assert solution.countCollisions("LLRR") == 0
