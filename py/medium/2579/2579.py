class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n - 1) + 1


solution = Solution()
assert solution.coloredCells(1) == 1
assert solution.coloredCells(2) == 5
assert solution.coloredCells(3) == 13
assert solution.coloredCells(4) == 25
assert solution.coloredCells(5) == 41
