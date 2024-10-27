from functools import cache
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows_number = len(matrix)
        cols_number = len(matrix[0])

        @cache
        def dfs(r, c):
            if r == rows_number or c == cols_number or matrix[r][c] == 0:
                return 0

            length = 1 + min(
                dfs(r + 1, c),
                dfs(r, c + 1),
                dfs(r + 1, c + 1),
            )
            return length

        result = 0
        for row in range(rows_number):
            for col in range(cols_number):
                result += dfs(row, col)
        return result


solution = Solution()
m = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1],
]
assert solution.countSquares(m) == 15

m = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0],
]
assert solution.countSquares(m) == 7
