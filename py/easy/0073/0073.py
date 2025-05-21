class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()
        for r, row in enumerate(matrix):
            for c, item in enumerate(row):
                if item == 0:
                    rows.add(r)
                    cols.add(c)
        for r, _ in enumerate(matrix):
            for c, _ in enumerate(row):
                if r in rows or c in cols:
                    matrix[r][c] = 0


solution = Solution()
m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(m)
assert m == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution.setZeroes(m)
assert m == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
