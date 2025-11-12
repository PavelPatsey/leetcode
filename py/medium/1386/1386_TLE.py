class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(n + 1)]
        for row, seat in reservedSeats:
            grid[row][seat] = 1
        counter = 0
        for i in range(1, n + 1):
            counter += get_counter(grid[i])
        return counter


def get_counter(row: list) -> int:
    if sum(row[2:10]) == 0:
        return 2
    if row[2] == 0:
        return 1
    if row[4] == 0:
        return 1
    if row[6] == 0:
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
