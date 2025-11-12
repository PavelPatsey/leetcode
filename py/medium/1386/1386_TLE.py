class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(n + 1)]
        # print(grid)
        for row, seat in reservedSeats:
            grid[row][seat] = 1
        counter = 0
        for i in range(1, n + 1):
            row = grid[i]
            if sum(row[2:10]) == 0:
                counter += 2
            elif sum(row[2:6]) == 0:
                counter += 1
            elif sum(row[4:8]) == 0:
                counter += 1
            elif sum(row[6:10]) == 0:
                counter += 1
            else:
                pass
        return counter


solution = Solution()
assert (
    solution.maxNumberOfFamilies(
        3,
        [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]],
    )
    == 4
)
