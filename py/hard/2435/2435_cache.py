from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        MOD = 10**9 + 7
        cache = [[[-1] * k for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r: int, c: int, remain: int) -> int:
            if r == ROWS or c == COLS:
                return 0
            new_remain = (remain + grid[r][c]) % k
            if (r, c) == (ROWS - 1, COLS - 1):
                return 1 if new_remain == 0 else 0
            if cache[r][c][remain] != -1:
                return cache[r][c][remain]
            down = dfs(r + 1, c, new_remain)
            right = dfs(r, c + 1, new_remain)
            cache[r][c][remain] = (down + right) % MOD
            return cache[r][c][remain]

        return dfs(0, 0, 0)


solution = Solution()
assert solution.numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3) == 2
assert solution.numberOfPaths([[0, 0]], 5) == 1
assert solution.numberOfPaths([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1) == 10
