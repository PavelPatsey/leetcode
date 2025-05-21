class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()
        for r, row in enumerate(matrix):
            for c, num in enumerate(row):
                if num == 0:
                    rows.add(r)
                    cols.add(c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows or c in cols:
                    matrix[r][c] = 0


solution = Solution()
m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(m)
assert m == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution.setZeroes(m)
assert m == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
