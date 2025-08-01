class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            last = res[-1]
            row = [last[0]] + [x + y for x, y in zip(last, last[1:])] + [last[-1]]
            res.append(row)
        return res


solution = Solution()
assert solution.generate(1) == [[1]]
assert solution.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
