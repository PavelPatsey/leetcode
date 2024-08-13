from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sorted_candidates = sorted(candidates)

        def backtrack(cur, pos, target):
            if target == 0:
                result.append(cur.copy())
            if target <= 0:
                return

            previous = -1
            for i in range(pos, len(sorted_candidates)):
                if sorted_candidates[i] == previous:
                    continue
                cur.append(sorted_candidates[i])
                backtrack(cur, i + 1, target - sorted_candidates[i])
                cur.pop()
                previous = sorted_candidates[i]

        backtrack([], 0, target)
        return result


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
