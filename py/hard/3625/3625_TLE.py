from itertools import combinations


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        res = 0
        for points in combinations(points, 4):
            if is_suitable(points):
                res += 1
        return res


def get_k_b(segment) -> tuple[float, float]:
    """
    y = kx+b
    """
    p1, p2 = segment
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        return float("inf"), x1  # hack b is not x
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return k, b


def is_trapezoid(segment1, segment2) -> bool:
    k1, b1 = get_k_b(segment1)
    k2, b2 = get_k_b(segment2)
    return k1 == k2 and b1 != b2


def is_suitable(points) -> bool:
    p1, p2, p3, p4 = points
    return (
        is_trapezoid((p1, p2), (p3, p4))
        or is_trapezoid((p1, p3), (p2, p4))
        or is_trapezoid((p1, p4), (p2, p3))
    )


solution = Solution()
assert solution.countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]) == 2
assert solution.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]) == 1
assert solution.countTrapezoids([[82, 7], [82, -9], [82, -52], [82, 78]]) == 0
