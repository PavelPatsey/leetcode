from typing import List


class Solution:
    @staticmethod
    def _equal_rows_number(matrix: List[List[int]]):
        return sum(True for row in matrix if len(set(row)) == 1)

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cols_number = len(matrix[0])

        def backtrack(m, i):
            if i == cols_number:
                return self._equal_rows_number(m)
            a = backtrack(m.copy(), i + 1)
            new_matrix = m.copy()
            for row in new_matrix:
                row[i] = 1 - row[i]
            b = backtrack(new_matrix, i + 1)
            return max(a, b)

        return backtrack(matrix, 0)


solution = Solution()
assert solution._equal_rows_number([[0, 1], [1, 1]]) == 1
assert solution._equal_rows_number([[0, 1], [1, 1], [0, 0]]) == 2

assert solution.maxEqualRowsAfterFlips([[0, 1], [1, 1]]) == 1
assert solution.maxEqualRowsAfterFlips([[0, 1], [1, 0]]) == 2
assert solution.maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]) == 2
