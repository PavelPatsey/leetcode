from operator import itemgetter


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        vals = sorted(intervals, key=itemgetter(0, 1))
        res = [vals[0]]
        for val in vals:
            if is_intersect(res[-1], val):
                res[-1][1] = max(res[-1][1], val[1])
            else:
                res.append(val)
        return res


def is_intersect(a: list, b: list) -> bool:
    return a[1] >= b[0]


solution = Solution()
assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
    [1, 6],
    [8, 10],
    [15, 18],
]
assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
assert solution.merge([[4, 7], [1, 4]]) == [[1, 7]]
assert solution.merge([[1, 4], [2, 3]]) == [[1, 4]]
