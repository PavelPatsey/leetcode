from collections import defaultdict
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows_number, cols_number = len(matrix), len(matrix[0])
        dp = defaultdict(int)

        result = 0
        for r in range(rows_number):
            for c in range(cols_number):
                if matrix[r][c]:
                    dp[(r, c)] = 1 + min(
                        dp[(r - 1, c)],
                        dp[(r, c - 1)],
                        dp[(r - 1, c - 1)],
                    )
                result += dp[(r, c)]
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
