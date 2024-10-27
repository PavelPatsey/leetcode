from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows_number = len(matrix)
        cols_number = len(matrix[0])
        counter = 0
        for r in range(rows_number):
            for c in range(cols_number):
                step = 0
                while (
                    r + step < rows_number
                    and c + step < cols_number
                    and (
                        partial_sum := self.partial_sum(matrix, r, c, step)
                        == (step + 1) ** 2
                    )
                ):
                    counter += partial_sum
                    step += 1
        return counter

    @staticmethod
    def partial_sum(matrix, row, col, step):
        partial_sum = 0
        for r in range(row, row + step + 1):
            partial_sum += sum(matrix[r][col : col + step + 1])
        return partial_sum


solution = Solution()
m = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1],
]


assert solution.partial_sum(m, 0, 0, 0) == 0
assert solution.partial_sum(m, 0, 0, 1) == 3
assert solution.partial_sum(m, 0, 0, 2) == 7
assert solution.partial_sum(m, 1, 1, 1) == 4
assert solution.partial_sum(m, 0, 1, 2) == 9

assert solution.countSquares(m) == 15


m = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0],
]
assert solution.countSquares(m) == 7
