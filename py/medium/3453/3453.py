EPSILON = 1e-05


class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        total = 0
        max_y = 0
        for _, y, l in squares:
            total += l**2
            max_y = max(max_y, y + l)
        ref = total / 2
        left, right = 0, max_y
        while abs(left - right) > EPSILON:
            mid = (left + right) / 2
            if calculate_bottom_half(squares, mid) >= ref:
                right = mid
            else:
                left = mid
        return left


def calculate_bottom_half(squares: list[list[int]], y_ref: float) -> float:
    res = 0
    for x, y, l in squares:
        if y < y_ref:
            res += l * min(y_ref - y, l)
    return res


solution = Solution()
assert abs(solution.separateSquares([[0, 0, 1], [2, 2, 1]]) - 1) < EPSILON
assert abs(solution.separateSquares([[0, 0, 2], [1, 1, 1]]) - 1.16667) < EPSILON
