from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        len_rows = len(grid)
        len_cols = len(grid[0])
        right = 0, 1
        down = 1, 0
        dirs = [right, down]
        res = 0

        def dfs(r: int, c: int, visited: set, total: int):
            if not (0 <= r < len_rows and 0 <= c < len_cols):
                return
            if (r, c) in visited:
                return
            new_visited = visited | {(r, c)}
            new_total = (total + grid[r][c]) % k
            if (r, c) == (len_rows - 1, len_cols - 1):
                if new_total == 0:
                    nonlocal res
                    res += 1
                return

            for dr, dc in dirs:
                dfs(r + dr, c + dc, new_visited, new_total)

        dfs(0, 0, set(), 0)
        return res


solution = Solution()
assert solution.numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3) == 2
assert solution.numberOfPaths([[0, 0]], 5) == 1
assert solution.numberOfPaths([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1) == 10
