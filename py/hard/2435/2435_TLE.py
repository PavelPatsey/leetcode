from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = [(0, 1), (1, 0)]
        res = 0

        def dfs(r: int, c: int, total: int):
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return
            new_total = (total + grid[r][c]) % k
            if (r, c) == (ROWS - 1, COLS - 1):
                if new_total == 0:
                    nonlocal res
                    res += 1
                return
            for dr, dc in DIRS:
                dfs(r + dr, c + dc, new_total)

        dfs(0, 0, 0)
        return res


solution = Solution()
assert solution.numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3) == 2
assert solution.numberOfPaths([[0, 0]], 5) == 1
assert solution.numberOfPaths([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1) == 10
