class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        grid = {}
        counter = 2 * n
        for row, seat in reservedSeats:
            if row not in grid:
                seats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                c = 2
                grid[row] = {"c": c, "seats": seats}
            else:
                c = grid[row]["c"]
            if c > 0:
                grid[row]["seats"][seat] = 1
                c2 = get_counter(grid[row]["seats"])
                grid[row]["c"] = c2
                dc = c2 - c
                counter += dc
        return counter


def get_counter(row: list) -> int:
    if sum(row[2:10]) == 0:
        return 2
    if sum(row[2:6]) == 0:
        return 1
    if sum(row[4:8]) == 0:
        return 1
    if sum(row[6:10]) == 0:
        return 1
    return 0


solution = Solution()
assert (
    solution.maxNumberOfFamilies(
        3,
        [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]],
    )
    == 4
)
assert solution.maxNumberOfFamilies(4, [[4, 3], [1, 4], [4, 6], [1, 7]]) == 4
