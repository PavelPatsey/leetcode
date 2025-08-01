class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            last = res[-1]
            item = [last[0]] + [x + y for x, y in zip(last, last[1:])] + [last[-1]]
            res.append(item)
        return res


solution = Solution()
assert solution.generate(1) == [[1]]
assert solution.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
