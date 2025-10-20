class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for op in operations:
            if op[1] == "+":
                x += 1
            else:
                x -= 1
        return x


class Solution2:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum(map(lambda x: 1 if "+" in x else -1, operations))


solution = Solution()
assert solution.finalValueAfterOperations(["--X", "X++", "X++"]) == 1
assert solution.finalValueAfterOperations(["++X", "++X", "X++"]) == 3
assert solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0

solution_2 = Solution2()
assert solution.finalValueAfterOperations(["--X", "X++", "X++"]) == 1
assert solution.finalValueAfterOperations(["++X", "++X", "X++"]) == 3
assert solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0
