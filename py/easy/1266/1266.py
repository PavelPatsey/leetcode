class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        res = 0
        for a, b in zip(points, points[1:]):
            x0, y0 = a
            x1, y1 = b
            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            res += max(dx, dy)
        return res


solution = Solution()
assert solution.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]) == 7
assert solution.minTimeToVisitAllPoints([[3, 2], [-2, 2]]) == 5
