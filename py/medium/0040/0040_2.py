from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, path, total):
            if total == target:
                res.append(path[:])
                return
            if i >= len(candidates) or total > target:
                return

            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i = i + 1
            backtrack(i + 1, path, total)

        candidates.sort()
        res = []
        backtrack(0, [], 0)
        return res


solution = Solution()
assert solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6],
]

assert solution.combinationSum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]


n = 10
assert solution.combinationSum2([1] * 1_000, n) == [[1] * n]
