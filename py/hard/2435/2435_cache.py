from typing import List
from functools import cache


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = [(0, 1), (1, 0)]
        MOD = 10**9 + 7

        @cache
        def dfs(r: int, c: int, total: int) -> int:
            if r == ROWS or c == COLS:
                return 0
            new_total = (total + grid[r][c]) % k
            if (r, c) == (ROWS - 1, COLS - 1):
                return 1 if new_total == 0 else 0
            lst = [dfs(r + dr, c + dc, new_total) for dr, dc in DIRS]
            sum_lst = sum(lst)
            return sum_lst % MOD

        return dfs(0, 0, 0)


solution = Solution()
assert solution.numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3) == 2
assert solution.numberOfPaths([[0, 0]], 5) == 1
assert solution.numberOfPaths([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1) == 10
