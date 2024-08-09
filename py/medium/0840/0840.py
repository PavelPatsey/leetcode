from typing import List


class Solution:
    @staticmethod
    def is_magic_matrix(matrix, i, j):
        elements = set()
        for r in range(i, i + 3):
            for c in range(j, j + 3):
                if 1 <= matrix[r][c] <= 9:
                    elements.add(matrix[r][c])
        if len(elements) != 9:
            return False

        a = sum(matrix[i][j : j + 3])
        for x in range(1, 3):
            if a != sum(matrix[i + x][j : j + 3]):
                return False
        for x in range(3):
            if a != matrix[i][j + x] + matrix[i + 1][j + x] + matrix[i + 2][j + x]:
                return False
        if a != matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2]:
            return False
        if a != matrix[i + 2][j] + matrix[i + 1][j + 1] + matrix[i][j + 2]:
            return False
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row_max = len(grid)
        col_max = len(grid[0])
        counter = 0
        for row in range(row_max - 2):
            for col in range(col_max - 2):
                if self.is_magic_matrix(grid, row, col):
                    counter += 1
        return counter


solution = Solution()
assert solution.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]) == 1
assert solution.numMagicSquaresInside([[8]]) == 0
assert solution.numMagicSquaresInside([[2, 7, 6], [1, 5, 9], [4, 3, 8]]) == 0
assert solution.numMagicSquaresInside([[5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 0
