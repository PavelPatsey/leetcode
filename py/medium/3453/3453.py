EPSILON = 1e-05


class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        ys = set()
        squares = sorted(squares, key=lambda x: x[1])
        total = 0
        y_left = float("inf")
        y_right = -float("inf")
        for _x, y, l in squares:
            total += l**2
            y_left = min(y_left, y)
            y_right = max(y_right, y + l)
            ys.add(y)
            ys.add(y + l)
        ref = total / 2
        for y_ref in sorted(ys):
            half = calculate_bottom_half(squares, y_ref)
            if are_equal(half, ref):
                return y_ref
        y_ref = (y_left + y_right) / 2
        half = calculate_bottom_half(squares, y_ref)
        while not are_equal(half, ref):
            if half > ref:
                y_right = y_ref
            else:
                y_left = y_ref
            y_ref = (y_left + y_right) / 2
            half = calculate_bottom_half(squares, y_ref)
        return y_ref


def calculate_bottom_half(squares: list[list[int]], y_ref: float) -> float:
    res = 0
    for x, y, l in squares:
        if y_ref > y + l:
            res += l**2
        elif y <= y_ref <= y + l:
            res += l * (y_ref - y)
        elif y_ref < y:
            pass
        else:
            raise Exception("invalid case!")
    return res


def are_equal(a: float, b: float, epsilon=EPSILON) -> bool:
    return abs(a - b) < epsilon


solution = Solution()
assert are_equal(solution.separateSquares([[0, 0, 1], [2, 2, 1]]), 1) is True
assert are_equal(solution.separateSquares([[0, 0, 2], [1, 1, 1]]), 1.16667) is True
