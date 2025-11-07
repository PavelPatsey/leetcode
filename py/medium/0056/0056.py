from operator import itemgetter


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        vals = sorted(intervals, key=itemgetter(0, 1))
        res = []
        i = 0
        while i < len(vals) - 1:
            a = vals[i]
            b = vals[i + 1]
            if is_intersect(a, b):
                vals[i + 1] = merge(a, b)
            else:
                res.append(vals[i])
            i += 1
        if i == len(vals) - 1:
            res.append(vals[i])
        return res


def is_intersect(a: list, b: list) -> bool:
    return a[1] >= b[0]


def merge(a: list, b: list) -> list:
    return [min(a[0], b[0]), max(a[1], b[1])]


solution = Solution()
assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
    [1, 6],
    [8, 10],
    [15, 18],
]
assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
assert solution.merge([[4, 7], [1, 4]]) == [[1, 7]]
assert solution.merge([[1, 4], [2, 3]]) == [[1, 4]]
