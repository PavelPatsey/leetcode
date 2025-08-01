class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            blank = [0] + res[-1] + [0]
            row = [x + y for x, y in zip(blank, blank[1:])]
            res.append(row)
        return res


solution = Solution()
assert solution.generate(1) == [[1]]
assert solution.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
