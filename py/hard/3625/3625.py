from itertools import combinations


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        res = 0
        for points in combinations(points, 4):
            if is_trapezoid(points):
                res += 1
        return res


def get_k(segment) -> float:
    p1, p2 = segment
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        return float("inf")
    return (y2 - y1) / (x2 - x1)


def is_parallel(segment1, segment2) -> bool:
    k1 = get_k(segment1)
    k2 = get_k(segment2)
    return k1 == k2


def is_trapezoid(points) -> bool:
    p1, p2, p3, p4 = points
    return (
        is_parallel((p1, p2), (p3, p4))
        or is_parallel((p1, p3), (p2, p4))
        or is_parallel((p1, p4), (p2, p3))
    )


solution = Solution()
assert solution.countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]) == 2
assert solution.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]) == 1
