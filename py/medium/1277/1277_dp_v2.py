from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows_number, cols_number = len(matrix), len(matrix[0])
        dp = matrix
        res = 0

        for r in range(rows_number):
            for c in range(cols_number):
                if dp[r][c] and r != 0 and c != 0:
                    dp[r][c] = 1 + min(
                        dp[r - 1][c],
                        dp[r][c - 1],
                        dp[r - 1][c - 1],
                    )
                res += dp[r][c]
        return res


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
