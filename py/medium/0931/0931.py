from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        len_rows = len_columns = len(matrix)
        dp = [[float("inf")] * len_columns for _ in range(len_rows)]
        dp[-1] = matrix[-1]

        for i in reversed(range(len_rows - 1)):
            for j in range(len_columns):
                dp[i][j] = matrix[i][j] + min(
                    dp[i + 1][j],
                    dp[i + 1][j - 1] if j > 0 else float("inf"),
                    dp[i + 1][j + 1] if j < len_columns - 1 else float("inf"),
                )
        return min(dp[0])


solution = Solution()
assert solution.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
assert solution.minFallingPathSum([[-19, 57], [-40, -5]]) == -59
