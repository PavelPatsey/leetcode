from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sorted_candidates = sorted(candidates)

        def dfs(i, sub_list, sub_sum):
            if sub_sum == target and sub_list not in result:
                result.append(sub_list)
                return
            if sub_sum > target:
                return
            if i >= len(sorted_candidates):
                return
            dfs(
                i + 1, sub_list + [sorted_candidates[i]], sub_sum + sorted_candidates[i]
            )
            dfs(i + 1, sub_list.copy(), sub_sum + 0)

        dfs(0, [], 0)
        return result


solution = Solution()
assert solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6],
]

assert solution.combinationSum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
