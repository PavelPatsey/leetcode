from typing import List


class Solution:
    @staticmethod
    def is_matrix_magic(matrix):
        assert len(matrix) == len(matrix[0]) == 3

        a = sum(matrix[0])
        b = sum(matrix[1])
        c = sum(matrix[2])
        d = matrix[0][0] + matrix[1][1] + matrix[2][2]
        e = matrix[2][0] + matrix[1][1] + matrix[0][2]
        for s in (b, c, d, e):
            if s != a:
                return False
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        pass


solution = Solution()
assert solution.is_matrix_magic([[4, 3, 8], [9, 5, 1], [2, 7, 6]]) is True
assert solution.is_matrix_magic([[1, 2, 3], [1, 1, 1], [1, 1, 1]]) is False

assert solution.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]) == 1
